from pathlib import Path
from PIL import Image, ImageDraw
from pypdf import PdfReader
import pdfplumber

root = Path(__file__).resolve().parent
pages = sorted(root.glob('final-page-*.png'))
for offset in range(0, len(pages), 8):
    group = pages[offset:offset + 8]
    canvas = Image.new('RGB', (4 * 320, 2 * 485), '#dddddd')
    draw = ImageDraw.Draw(canvas)
    for i, path in enumerate(group):
        image = Image.open(path).convert('RGB')
        image.thumbnail((302, 452))
        x = (i % 4) * 320 + 9
        y = (i // 4) * 485 + 22
        canvas.paste(image, (x, y))
        draw.text((x, y - 17), path.stem, fill='black')
    canvas.save(root / f'overview-{offset // 8 + 1}.png')

with pdfplumber.open(root.parent / 'Easy_Fuel_User_Manual.pdf') as pdf:
    for i, page in enumerate(pdf.pages, 1):
        bad = [word['text'] for word in page.extract_words() if word['x0'] < 45 or word['x1'] > page.width - 45]
        if bad:
            raise RuntimeError(f'Page {i} exceeds horizontal margins: {bad}')
        text = page.extract_text()
        if len(text) < 150:
            print(f'Low density page {i}: {len(text)} characters')
        print(f'Page {i}: {text.splitlines()[1][:110]}')
print(f'Checked {len(pages)} rendered pages and PDF margins.')
