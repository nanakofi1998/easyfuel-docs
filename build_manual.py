"""Build the printable manual from its editable Markdown source."""
from pathlib import Path
import html
import re

from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, CondPageBreak
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / 'Easy_Fuel_User_Manual.md'
text = SOURCE.read_text(encoding='utf-8')
lines = text.splitlines()


def inline(value):
    value = html.escape(value, quote=False)
    value = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', value)
    return re.sub(r'`([^`]+)`', r'<b>\1</b>', value)


def anchor(title):
    return re.sub(r'[^a-z0-9]+', '-', title.lower()).strip('-')


styles = getSampleStyleSheet()
for style in styles.byName.values():
    style.textColor = colors.black
styles.add(ParagraphStyle(name='ManualTitle', fontName='Helvetica-Bold', fontSize=27, leading=32, spaceAfter=14))
styles.add(ParagraphStyle(name='ManualSection', fontName='Helvetica-Bold', fontSize=18, leading=23, spaceBefore=10, spaceAfter=12, keepWithNext=True))
styles.add(ParagraphStyle(name='ManualSubsection', fontName='Helvetica-Bold', fontSize=12, leading=16, spaceBefore=14, spaceAfter=7, keepWithNext=True))
styles.add(ParagraphStyle(name='ManualBody', fontName='Helvetica', fontSize=10, leading=14.2, spaceAfter=8, allowWidows=0, allowOrphans=0))
styles.add(ParagraphStyle(name='ManualList', parent=styles['ManualBody'], leftIndent=18, firstLineIndent=-18, spaceAfter=5))
styles.add(ParagraphStyle(name='ManualCell', fontName='Helvetica', fontSize=9, leading=12, spaceAfter=0, alignment=TA_LEFT))
styles.add(ParagraphStyle(name='ManualTableHeader', parent=styles['ManualCell'], fontName='Helvetica-Bold', textColor=colors.white))

story = []
html_parts = []
outline = []
index = 0
while index < len(lines):
    line = lines[index].strip()
    if not line:
        index += 1
        continue
    if line.startswith('|'):
        rows = []
        while index < len(lines) and lines[index].strip().startswith('|'):
            cells = [cell.strip() for cell in lines[index].strip().strip('|').split('|')]
            if not all(re.fullmatch(r':?-+:?', cell) for cell in cells):
                rows.append(cells)
            index += 1
        columns = len(rows[0])
        widths = [125, 135, 235] if columns == 3 else [155, 340]
        data = [[Paragraph(inline(cell), styles['ManualTableHeader'] if row_number == 0 else styles['ManualCell']) for cell in row] for row_number, row in enumerate(rows)]
        table = Table(data, colWidths=widths, repeatRows=1, hAlign='LEFT')
        table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#353535')),
            ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#F5F5F5')]),
            ('GRID', (0, 0), (-1, -1), 0.4, colors.HexColor('#D9D9D9')),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ('LEFTPADDING', (0, 0), (-1, -1), 8),
            ('RIGHTPADDING', (0, 0), (-1, -1), 8),
            ('TOPPADDING', (0, 0), (-1, -1), 7),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 7),
        ]))
        story.extend([table, Spacer(1, 12)])
        html_parts.append('<div class="table-wrap"><table><thead><tr>' + ''.join('<th>' + inline(cell) + '</th>' for cell in rows[0]) + '</tr></thead><tbody>' + ''.join('<tr>' + ''.join('<td>' + inline(cell) + '</td>' for cell in row) + '</tr>' for row in rows[1:]) + '</tbody></table></div>')
        continue
    if line.startswith('#'):
        level = len(line) - len(line.lstrip('#'))
        title = line[level:].strip()
        key = anchor(title)
        if level == 2:
            if outline:
                story.append(CondPageBreak(280))
            outline.append((key, title))
            heading = Paragraph('<a name="' + key + '"/>' + inline(title), styles['ManualSection'])
            heading.manual_bookmark = (key, title)
            story.append(heading)
        else:
            story.append(Paragraph(inline(title), styles['ManualTitle'] if level == 1 else styles['ManualSubsection']))
        html_parts.append(f'<h{level} id="{key}">{inline(title)}</h{level}>')
        index += 1
        continue
    if re.match(r'^\d+\. ', line):
        number, content = line.split('. ', 1)
        story.append(Paragraph(number + '. ' + inline(content), styles['ManualList']))
        html_parts.append('<p class="step"><span>' + number + '.</span> ' + inline(content) + '</p>')
    else:
        paragraph = [line]
        while index + 1 < len(lines) and lines[index + 1].strip() and not re.match(r'^(#|\||\d+\. )', lines[index + 1].strip()):
            index += 1
            paragraph.append(lines[index].strip())
        value = ' '.join(paragraph)
        story.append(Paragraph(inline(value), styles['ManualBody']))
        html_parts.append('<p>' + inline(value) + '</p>')
    index += 1


def furniture(canvas, document):
    canvas.saveState()
    canvas.setFont('Helvetica', 8)
    canvas.setFillColor(colors.HexColor('#555555'))
    canvas.drawString(50, A4[1] - 30, 'EASY FUEL  /  USER MANUAL')
    canvas.drawRightString(A4[0] - 50, A4[1] - 30, '8 October 2026')
    canvas.drawString(50, 28, 'Edition 1.0  |  Role based operating guide')
    canvas.drawRightString(A4[0] - 50, 28, str(document.page))
    canvas.restoreState()


class ManualDocument(SimpleDocTemplate):
    def afterFlowable(self, flowable):
        if hasattr(flowable, 'manual_bookmark'):
            key, title = flowable.manual_bookmark
            self.canv.bookmarkPage(key)
            self.canv.addOutlineEntry(title, key, level=0)


pdf_path = ROOT / 'Easy_Fuel_User_Manual.pdf'
document = ManualDocument(str(pdf_path), pagesize=A4, rightMargin=50, leftMargin=50, topMargin=54, bottomMargin=48, title='Easy Fuel User Manual', author='Easy Fuel', allowSplitting=1)
document.build(story, onFirstPage=furniture, onLaterPages=furniture)

nav = ''.join(f'<a href="#{key}">{html.escape(title)}</a>' for key, title in outline)
template = '''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>Easy Fuel User Manual</title>
<style>
*{box-sizing:border-box}body{margin:0;color:#202020;background:#f3f4f6;font:15px/1.65 Arial,sans-serif;letter-spacing:0}nav{position:fixed;left:0;top:0;bottom:0;width:270px;overflow:auto;background:#fff;border-right:1px solid #ddd;padding:24px 20px}nav strong{display:block;margin-bottom:16px;font-size:19px;color:#111}nav a{display:block;color:#333;text-decoration:none;font-size:13px;line-height:1.4;padding:8px 0}nav a:hover{color:#ba5316}main{margin-left:270px;max-width:1090px;padding:48px 56px;background:#fff;min-height:100vh}h1{font-size:34px;line-height:1.2;margin-top:0;color:#000}h2{font-size:25px;margin-top:54px;padding-top:10px;scroll-margin-top:20px;color:#000}h3{font-size:18px;margin-top:30px;scroll-margin-top:20px;color:#000}p{margin:0 0 14px}.step{padding-left:26px;text-indent:-26px}.step span{display:inline-block;min-width:22px}.table-wrap{overflow:auto;margin:18px 0 24px}table{width:100%;border-collapse:collapse;font-size:13px}th,td{border:1px solid #d9d9d9;padding:10px 12px;text-align:left;vertical-align:middle}th{background:#353535;color:white}tbody tr:nth-child(even){background:#f5f5f5}td:first-child{width:30%}.edition{font-size:12px;color:#666}button{border:0;border-radius:4px;background:#e27225;color:#fff;padding:8px 14px;font-weight:600;cursor:pointer}
@media(max-width:900px){nav{position:static;width:auto;max-height:300px;border-right:0;border-bottom:1px solid #ddd}main{margin:0;padding:28px 22px}h1{font-size:28px}}
@media print{@page{size:A4;margin:18mm}body{background:#fff;font-size:10pt;line-height:1.45}nav,button{display:none}main{margin:0;padding:0;max-width:none}h1{font-size:24pt}h2{break-before:page;font-size:17pt;margin:0 0 14pt}h3{font-size:12pt;break-after:avoid}p{orphans:3;widows:3}table{font-size:9pt}thead{display:table-header-group}tr{break-inside:avoid}th,td{padding:7px}a{color:#000}*{-webkit-print-color-adjust:exact;print-color-adjust:exact}}
</style></head><body><nav><strong>Easy Fuel User Manual</strong>NAVIGATION<button onclick="window.print()">Print Manual</button></nav><main>CONTENT</main></body></html>'''
(ROOT / 'Easy_Fuel_User_Manual.html').write_text(template.replace('NAVIGATION', nav).replace('CONTENT', '\n'.join(html_parts)), encoding='utf-8')

reader = PdfReader(str(pdf_path))
pdf_text = '\n'.join(page.extract_text() for page in reader.pages)
required = ['Shop attendant POS and inventory', 'System administrator', 'OMC administrator', 'Station manager', 'Pump attendant mobile workflow', 'Troubleshooting', 'Create Category']
for heading in required:
    if heading not in pdf_text:
        raise RuntimeError('Missing manual topic: ' + heading)
print(f'Created manual PDF and HTML from {len(text.split())} words across {len(reader.pages)} PDF pages.')
