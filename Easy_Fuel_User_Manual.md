# Easy Fuel User Manual

Role based guide to fuel station operations and shop POS inventory

Edition 1.0 | Prepared 8 October 2026 | Application source baseline backendv2.0.0 and frontendv2.0.0

## 1 How to use this manual

This manual explains how to use Easy Fuel for platform administration, OMC administration, station management, pump attendant sales and the new shop attendant POS and inventory workspace. Start with signing in, then read the section for your assigned role. Use the daily checklists when training a new user or handing over a station.

An OMC is an Oil Marketing Company. Each OMC has its own users, stations, products, payment methods and records. Station users work within their assigned station. Menu visibility and available actions depend on the account role, assigned permissions and deployment configuration.

**Release distinction.** This guide is based on the application source, not a certification of a deployed production environment. A visible page, toast or green Live indicator does not by itself establish that an action has been saved, transmitted, paid or audited. Check the relevant record after an action. Procedures marked **Prototype** describe a UI demonstration and must not be used as proof of a real operational or financial event.

The shop POS and inventory workspace is currently a prototype. The station supervisor, OMC operations and audit workspaces also contain demonstration data. The cashier dashboard is a placeholder. The connected station manager and OMC admin workflows are documented separately.

### Contents

1. How to use this manual
2. Roles and workspaces
3. Sign in and account security
4. Common page controls
5. System administrator
6. OMC administrator
7. Station manager
8. Pump attendant mobile workflow
9. Station supervisor
10. OMC operations administrator
11. Audit risk and compliance
12. Shop attendant POS and inventory
13. Cashier and additional role accounts
14. Reading financial and stock figures
15. Troubleshooting
16. Operating checklists and glossary

## 2 Roles and workspaces

| Role | Workspace | Main responsibility |
| --- | --- | --- |
| System administrator | Platform sidebar | Create OMCs and users, configure tenant payment integrations and inspect transaction accounts and errors. |
| OMC administrator | OMC sidebar | Configure stations and master data; review station submissions, stock requests, expenses and variances. |
| Station manager | Station sidebar | Manage shift templates, readings, stock requests, receipts, reconciliation, reports and EOD. |
| Pump attendant | External mobile app | Sell fuel using assigned pumps and nozzles, validate cards/coupons and review own transactions. |
| Station supervisor | Header tabs | Delegated station operations; current dedicated workspace is a prototype. |
| OMC operations administrator | Header tabs | Station metadata, tanks and pump/nozzle setup; current dedicated workspace is a prototype. |
| Audit risk compliance officer | Header tabs | Read records and evidence without approving or altering station operations; current workspace is a prototype. |
| Shop attendant | Header tabs | Retail sales, inventory lookup and item creation, held baskets, cash drawer and retail shifts; currently a prototype. |
| Cashier | Cashier dashboard | Dedicated cashier dashboard is a placeholder in this source baseline. |

Additional role labels can share a workspace without receiving every action in that workspace. OMC owner and finance officer accounts route to the OMC portal; finance officer menus depend on their permissions. Read only auditor accounts share the audit workspace. System administrator aliases and specialist roles are covered in section 13.

**Fuel inventory and retail inventory are different.** Fuel uses tanks, pumps, nozzles and litre readings. Shop inventory uses item codes, SKUs, barcodes and unit quantities. Adding a shop item does not create a fuel product or change a fuel tank.

## 3 Sign in and account security

### 3.1 Web portal login

Before signing in, obtain your account email and initial password from your administrator. Open the approved Easy Fuel web address provided by your organisation.

1. Enter your email and password on Sign in.
2. Use the eye control to show or hide the password if necessary.
3. Select the sign in button once and wait for the response.
4. Complete email verification if the application requests it.
5. Complete the mandatory password change if this is your first login and your account requires it.
6. Wait for Welcome and the automatic redirect to your assigned workspace.

There is no role selector on the production login form. The server determines your account role and OMC. Do not enter an OMC security code into the login fields.

### 3.2 Email verification

Email OTP verification applies to system admin and OMC admin logins. Other role labels or deployment policies may be handled differently; follow the verification screen when it appears.

1. Open the newest verification email sent to your registered address.
2. Type the digits into the separate code boxes, or paste the whole code.
3. Verification starts automatically when the last digit is entered.
4. Wait for the verification result and Welcome before navigating away.
5. If no email arrives, wait until the resend timer allows another request, then select Resend once.

The resend cooldown is normally 30 seconds in the current configuration. The screen's countdown is authoritative. A resent code replaces the prior challenge state; use the latest email. Never send an OTP to support or another staff member.

### 3.3 First login password change and reset links

When a password change is required, enter a new password and the same value in Confirm password. The first login form does not require re-entering the temporary password. Follow the on-screen password rules. After a successful update, wait for the confirmation and redirect.

For a forgotten password, request an administrator-issued password reset link. Open the latest link, enter the new password twice and complete the reset. If the link has expired or was already used, ask for a new link. The reset link is private and should not be forwarded.

### 3.4 Session expiry and lock screen

Web access sessions normally use a two-hour access token. Near expiry, the application can display a 01:00 countdown and Keep Session Alive. Select that action while the refresh session remains valid. If renewal is refused or the timer expires, sign in again. Mobile session policies are separate.

Use the profile/account menu's Lock Screen or Lock Register action when leaving a shared device. Unlock with the credentials requested on the lock screen. Sign out at the end of your work; closing a browser tab is not an operational handover.

### 3.5 Profile settings and notifications

Open View Profile or Settings from the profile menu where available. Station manager profile details are read only; request an authorised change rather than editing identity data directly. System admin profile editing uses its own controls. Follow the role's actual form.

Appearance controls can include light, dark, system and Power BI modes, button colour, sidebar colour and header colour. Shop attendant navigation has no theme switch. Appearance choices do not change financial data.

Managers should review Workflow Defaults and Notifications and Security settings. Set a six-digit EOD PIN before submitting an EOD. Reset the PIN through its security form when required. Keep this PIN separate from an attendant login ID.

Open the notification bell to read messages. Mark as read acknowledges a message; the current notification policy may remove it after reading. Enable the notifications you actually need. Do not expect every module or every KPI to update live.

## 4 Common page controls

### 4.1 Navigation and details

Use the sidebar to open modules in the system admin, OMC admin and station manager portals. Expand a menu to see its submenus. In a collapsed sidebar, use its flyout menu. The shop and delegated role portals use header tabs instead of a sidebar. Breadcrumbs show the current page and, where supported, a link back to a parent page.

Many KPI cards open a right-side drawer. Select a card to inspect its breakdown, charts and supporting records. Some cards already contain a breakdown and do not open a drawer. A drawer's close control or the area outside it returns you to the page.

The vertical three-dot button in a row opens its action menu. Actions should match the record's current state: for example, an expired shift template needs reactivation, while an approved variance may need reopening rather than a second approval.

### 4.2 Search filters and pagination

1. Use Search to find a reference, name, code or another supported field.
2. Open Filters for advanced choices such as dates, station, product, status or risk.
3. Set the desired values and select the tick icon to Apply where provided.
4. Use the reset icon to restore defaults. Changing a draft filter does not necessarily change the report until Apply is selected.
5. Use left/right carets for paginated tables. Integrated registers commonly fetch 20 records per page; the page footer shows the actual total and page size.

Read the displayed period before comparing figures. Today, last seven days, last month and all time are different scopes. The station manager dashboard deliberately uses different periods for its KPI cards, weekly sales chart and recent transactions.

### 4.3 Charts exports and print

Hover over a chart to view a tooltip. Use supported legend entries to show or hide a series. Where chart-type pills exist, choose an available line, column, stacked or doughnut display. The available types vary by report.

Choose Export CSV for spreadsheet data or Export PDF for a formatted report. Apply the intended filters first. Print actions can print a single record or the displayed report; read the action name before proceeding. Fuel reports normally identify the OMC and may identify the station and generating user. Store exports according to your organisation's policy.

Some print controls are demonstration controls; the role section identifies these. A browser's Print dialog and a backend-generated PDF are different outputs. For example, the current manager EOD Print / PDF control uses the browser print workflow.

### 4.4 Loading and feedback

Skeleton placeholders indicate that page content is loading. Button spinners indicate an action in progress. Avoid clicking a submit button repeatedly. Success, warning and error messages explain the outcome. On the shop portal, compact toasts last about seven seconds and repeated messages are suppressed.

## 5 System administrator

Use this workspace for platform and tenant administration. Treat cross-OMC information as privileged data. The main operational modules verified in the source include OMC tenants, system users, public onboarding, transaction accounts, People's Pay integration and error logs. Other platform monitoring/control screens can still contain seeded demonstration records.

### 5.1 Create and maintain an OMC

Open Tenant and Portal Control > OMC Tenants.

1. Select Create OMC.
2. Enter the organisation name and the contact, business, website and subscription fields shown in the form.
3. Upload the organisation's logo. The current tenant-logo validation permits JPEG/JPG, PNG or SVG, up to 1 MB. This differs from the retail-item image rules.
4. Review the data and save once.
5. Confirm the new OMC appears in the register. Open its row details to inspect its information.
6. Use the relevant row action to edit, change its state or archive it when authorised. Read the confirmation before an archive action.

The server generates tenant identifiers. Do not manually invent or reuse OMC security identifiers. An OMC must exist before its admin account can be attached to it.

### 5.2 Create a tenant user

Open Tenant and Portal Control > Users and select Create User.

1. Select the intended role.
2. For an OMC user, select the correct OMC. The user must belong to that OMC.
3. Enter first name, last name, Ghana Card number, phone, date of birth and the other required identity fields.
4. Enter email for roles that require it. Pump attendant email can be optional.
5. Set the initial/temporary password or invitation fields shown, and the first-login reset option as appropriate.
6. Create the user, then confirm their role, OMC and status in the register.

Ghana Card format is GHA-123456789-1, with all 15 characters present. The form can insert separators while typing; the prefix alone is not a valid number. Active pump attendants receive a generated six-digit attendant ID through queued SMS where SMS delivery is configured. Keep that ID private.

Open row details to review identity information or use the provided edit/status action. Do not assume every visible role or permission control is connected simply because it appears in a dropdown. OMC user-management procedures are described in section 6.

### 5.3 Public onboarding and demo requests

Open Public Onboarding to review applications and demo enquiries from the external signup flow.

1. Select the appropriate applications or demo-requests view.
2. Search/filter to find a company or enquiry.
3. Open details and inspect contact information, uploaded logo, verification state and supporting information.
4. Assign a reviewer or request further information using the available action.
5. Approve or reject an eligible application with a clear decision reason where requested.
6. For demo enquiries, update the contact/scheduling state and record follow-up information in the supplied form.

An external application is not automatically equivalent to a fully operational tenant. Confirm conversion and account setup before providing production access.

### 5.4 Configure People's Pay for an OMC

Open Accounts and Transactions > People's Pay Integration. Obtain the correct merchant ID and API key through the authorised provider channel.

1. Select the configuration creation action.
2. Select the OMC and environment, Sandbox or Production.
3. Enter the merchant ID and API key. Enter a meaningful configuration reason; the current form requires at least 10 characters.
4. Save the configuration.
5. Use the row menu's Test Connection action and confirm the verified active state before the OMC starts MoMo collections.
6. To switch environments, choose Change Environment / Credentials. Use the environment-only option when reusing the existing credentials, then test the target environment.
7. Use View Configuration and View Audit Trail to review configuration history. Suspend only when authorised; suspension blocks new collections.

The current implementation requires connection verification. Do not assume a saved configuration is already active. Each OMC's credential version is retained for its existing transactions. Credentials must never be pasted into user messages, ordinary support notes or public exports.

### 5.5 Inspect transaction accounts

Open Transaction Accounts. The default period is Today.

1. Select Today, This Week, This Month or All Time, and the available tenant/status filters.
2. Inspect successful value, failed/pending records and the OMC breakdown.
3. Open the OMC drawer to inspect its account composition.
4. Open an individual transaction to review its reference, provider information, status and supporting details.
5. Export the scoped register when needed for an authorised review.

A pending provider transaction is not successful income. Use the recorded payment status and successful-value totals rather than summing every initiated request.

### 5.6 Inspect errors and platform screens

Open Audit and Compliance > Error Logs. Search/filter the available entries, expand a row and review its structured details. Where available, Run Provider Check tests configured People's Pay connectivity and records diagnostics. A successful connectivity check does not prove an unrelated payment completed.

Record the occurrence time, affected user/station, transaction reference and relevant error message when escalating. Exclude passwords, OTPs, API keys and access tokens.

Platform Operations, Security Center, QA and Release Control, Data and Backups, and several Audit and Compliance screens currently include demonstration records or controls in the shared operational UI. Use them for interface review only until your deployment confirms a connected service. In particular, a UI backup/restore action is not proof that a recoverable backup exists. System Settings and profile data have dedicated forms; only treat a setting as saved after the server confirms the change.

## 6 OMC administrator

The OMC workspace manages the station network belonging to your OMC. Configure active master data before station staff begin operations. Review approvals with the supporting evidence rather than acting on the KPI value alone.

### 6.1 Recommended setup order

1. Create active fuel products.
2. Create and activate the OMC's accepted payment methods.
3. Create expense categories and define whether approval is required.
4. Create station managers, pump attendants and cashiers as needed.
5. Complete station setup: station, tanks, pumps, staff, payments and products.
6. Set product prices with an appropriate effective date.
7. Ask the station manager to create shift templates and configure their EOD PIN.
8. Ask the system administrator to verify the OMC's People's Pay integration before MoMo collection starts.

### 6.2 Products and payment methods

For products, open Master Data Setup > Products and select Create New Fuel Type.

1. Enter product name and code, select category/unit and set the minimum stock alert.
2. Choose its active/inactive state and save.
3. Confirm the record in Fuel Types Management. Use search, filters, pagination and the view/edit/deactivate actions as needed.

Fuel pricing is maintained in Price (Px) Management, not in product creation. Codes are used widely in operational reports; choose recognisable codes and avoid renaming an item to disguise a different product.

For payments, open Payment Method Setup, enter a method name and code, set the status toggle and save. These are configurable OMC records. Stations select active methods from this list. Where the implementation exposes a system processing type/provider mapping, use the appropriate supported mapping; a newly invented label does not create a new external payment processor.

### 6.3 Expense categories

Open Expense Categories and use the creation action. Enter the category fields, choose the allowed groups, approval requirement and status, then save. A category can belong to multiple configured groups. Managers select active categories from their OMC rather than typing an unrelated category name.

Categories requiring review produce pending expenses. Categories configured not to require approval can produce automatically approved records with the explanation that approval is not required. Configure this policy deliberately; it is different from permitting a maker to approve their own review-required expense.

### 6.4 Complete the station wizard

Open Stations and select Create New Station. The six steps are saved progressively. Earlier steps are not freely revisited through the wizard. If setup is interrupted, use Continue Setup in that station's action menu to resume the saved step rather than creating a duplicate station.

1. **Station.** Enter identity, ownership, location, address, permit/licence and operating fields. Select country and currency using the searchable selects. Set cut-off time, expense limit, variance tolerance and Require EOD Submission. Set tank-reading and temperature/calibration policy carefully. Save and continue.
2. **Tanks.** Use Add Tank for each tank. Select an active OMC product; enter code, name, type, capacity, initial stock, minimum threshold and reorder level. Remove unwanted draft tanks with the delete icon. Submit all completed tank forms using Save and Continue.
3. **Pumps.** Add each pump with its code/name/type and manufacturer/model where applicable. Add one or more nozzles inside a pump. Each nozzle needs a code and a connection to a tank at this station, plus nozzle/meter type. Remove unwanted draft pumps/nozzles with their delete icons. Save the batch and continue.
4. **Staff.** Choose a supported role to populate active eligible users. Select users for the station. The global selected-user row shows selections across roles; use its cross to remove an incorrect selection. Already-assigned station staff are not available for a conflicting station assignment. Save and continue.
5. **Payments.** Select the active OMC payment-method code pills accepted at this station. Save and continue.
6. **Products.** Select active product pills allowed at this station. Complete setup and return to Stations.

The Brand/OMC field is controlled by your tenant. You do not supply another tenant's identity. Do not activate a station until its setup is complete and mappings are checked.

Temperature choices such as Record Only and Apply Correction are not interchangeable. Some calibration/device choices are reserved for later integration. Selecting a future/device option does not connect a tank gauge; confirm support before relying on automatic conversion.

### 6.5 Maintain stations tanks pumps and staff

Open a station's action menu to view details, edit station metadata, manage tanks/pumps/staff/payment methods/products, change status or continue incomplete setup. The setup progress bar helps identify unfinished records.

In Tanks Setup, select the station before creating a tank. Enter the product, capacity, current stock and thresholds. Editing stock metadata should not be used to conceal a physical shortage; use the proper reading/correction workflow and supporting reason.

In Nozzle/Pump Configuration, select the station first. Add or edit its pumps and map nozzles to its active tanks. The frontend displays active nozzles. Removing a nozzle in Edit Pump is persisted when Save Pump succeeds. Removed nozzles are retained for history and excluded from current configuration; a physical historical transaction is not deleted.

In User Management > Station Assignment, select role and station, choose eligible unassigned users and assign the selected users. Verify the table afterwards. Use the unassign action with a reason for a genuine reassignment. A staff member already assigned to another station must not be selected for a second conflicting station assignment.

### 6.6 Users and access control

Open Users to create a tenant user. Select an allowed role, complete the required identity/contact fields, enter password and confirm password, then create once. Email is optional only for a pump attendant. Reset Form clears unsaved fields. The server attaches the OMC from your session; you cannot create a system administrator from the OMC portal.

The paginated user register supports search and filters. Review View Profile, Edit, Deactivate and Send Password Reset Link where available. Pump attendant rows can offer Resend Attendant ID for queued SMS delivery when the original message was not received. Use status changes with an operational reason. Editing identity data is not the same as creating a new user.

Open Access Control for permission definitions and assignments. Use Create Permission, select a role, choose permitted modules and actions, then save. The form supports multiple module/action pills. Assign permissions or restrictions through this page's supported controls. Default role access applies until modified by an authorised override. The general Users row menu does not provide the permission assignment entry in the current UI.

Some legacy role-change displays remain unintegrated. Confirm the actual saved role before communicating new access to the user. Do not grant self-approval casually.

### 6.7 Set or schedule a price

Open Sales > Price (Px) Management.

1. Use Price Setup for a product with no initial configuration, or Update Price for an existing product.
2. Select the product, enter the price per litre and choose the effective date/time. Use Set Now only when the new price should apply immediately.
3. Enter the price-change reason and save.
4. Confirm the active price or inspect View Scheduled Prices for future changes.
5. Edit or cancel a pending scheduled change if the plan changes before activation.
6. Use Current Price Configuration and Price Adjustment History to review the effective state and audit trail.

Prices support up to three decimal places. A new price applies to new transactions using their effective timestamp. Completed sales retain their transaction price snapshot. Do not expect historical revenue to be recalculated at today's price.

### 6.8 Approve requisitions and dispatch stock

Open Approvals and Verifications > Requisition Approvals.

1. Apply station, status, product or date filters as needed.
2. Open Approve for a pending requisition and review its station, receiving tank/product, requested quantity, ETA and remarks.
3. Enter the approved quantity. If it differs from the requested quantity, enter the increase/decrease reason requested by the form.
4. Review the confirmation and approve once, or use Decline with a reason.
5. For an eligible approved requisition, choose Dispatch.
6. Check the read-only request/product/requested/approved quantities. Enter the actual quantity to dispatch, waybill number, dispatch date, driver, vehicle, dispatched-by information and notes.
7. Submit and confirm the dispatch record and requisition state.

Bulk approve/decline actions apply to selected eligible records only. Review each item before selecting all pending. Approval counts should describe approval events even after stock is dispatched. A dispatched quantity is not automatically a received quantity; the station manager records the actual receipt.

### 6.9 Review EOD submissions and variances

Open Pending Submissions. Search/filter the inbox and open a record with View. Review the business date, station, submitter, sales/collection totals, risk, variance and attached evidence. Use the eligible Approve, Reject or Flag for Investigation action. Supply a reason for rejection or investigation and read the confirmation before acting.

Variance Review and Stock Variance provide related views of discrepancy records. Inspect expected and physical figures, litres, financial impact, source, risk and prior decisions. Attach evidence where the review form allows it. Do not approve solely because a variance lies within tolerance; tolerance is an investigation signal, not a replacement for a checker.

After a final decision, use the supported reopen/review workflow with a reason if a mistake is discovered. Do not repeatedly approve the same record or create a second contradictory decision from the other variance page. A maker normally cannot approve their own review-required submission without an explicitly authorised exception.

### 6.10 Sales stock and windfall analytics

Use Daily Sales Sheet for product sales across the OMC network. Apply the desired filters. Cards can show zero-valued products when there are no matching sales. Open a card to inspect station breakdowns. Recent transaction records show their payment status; a zero total is different from a failed data fetch.

Use Sales and Cash Summary to compare station revenue and actual collections, review banking and expense information, and export a filtered report. Use Sales Analysis for date/product/station drill-down, daily/weekly/monthly views, trends and detailed sales records. The historical price shown for a sale should be assessed against its transaction date, not today's pump price.

Use Stock Analysis for opening/closing stock, receipts, sales, turnover, cover and movement trends. Read the period and station scope before comparing stations. Use Stock Variance for measured stock discrepancies rather than treating the operational tank balance as a fresh physical measurement.

Windfall Analysis examines the inventory price-change effect. Use Analytics for gains/losses by station and product, and Investigations for the kanban workflow. Open a case to inspect its cause/evidence and move it through an eligible status. Moves can be throttled; wait after an update and verify it saved. A windfall estimate is not automatically realised profit or a stock adjustment.

### 6.11 Accounting and finance

Use Cash and Collections Reconciliation to compare expected and reported actual collections by station/date. Read the default period label; the normal recent window is seven days unless filters change it. Open KPI drawers for detail, then inspect the register and exports.

Use Banking (Deposits) for deposit trends, method composition, station totals and slip records. Open details and the relevant review action to inspect the uploaded slip, amount, method, date and station. Banking Variance compares expected and actual banking figures; review the source records before assigning a cause or decision.

Use Station Expenses for expenses submitted by stations under your OMC. Review category, amount, taken-from-sales value, submitter, receipt and status before approving, rejecting or flagging an eligible item. Expenses marked as not requiring approval follow their category policy.

Use Director/Special Expenses to record authorised OMC/director expenses. The requester is the logged-in user. Choose an appropriate category and funding/payment details, attach the receipt and supply notes. Daily Expense Sheet consolidates station expenses for a chosen day or range. KPIs and Financial Exports summarises financial components and offers scoped exports; validate the period and contributing records before distribution.

Expected gross collections and expense deductions should be read as separate lines. Do not deduct the same expense twice or count a deposited cash amount as both cash still in the drawer and money already banked.

### 6.12 Cards and coupons

Open Generate Card. Create an institution where required, then enter card owner, institution, limit and limit type, Currency or Litres. Generate the card and verify the institution, owner, status and limit. A new card starts at zero balance. Use Top Up to fund it without exceeding its limit. Choose its available design shade, preview it, export the coloured PDF or share by email using the receiver's address. Verify the QR appears on the generated document.

Card QR verification confirms authenticity/status; it does not perform a sale. The attendant must validate and process the card through the mobile payment workflow. Suspension/inactivity and attempt limits can stop further use.

Open Generate Coupons. Choose a denomination of GHS 50, 100, 200, 500 or 1,000; choose the offered digital/hardcopy mode and batch quantity. A batch is limited to 100 coupons. Read daily/monthly/yearly allowance and remaining usage before generating. Normal daily allowance is 500 per generator unless an authorised configuration changes it. A limit change requires a reason through supported administrative controls.

Use batch details to inspect coupon codes and status. Export eligible hardcopy coupons for printing; the layout includes separation guides. Printed graphics do not constitute a physical hologram or guarantee counterfeit-proof paper. Use digital secure links when sharing individual downloads: each coupon gets its own expiring one-use download link. Email/share generation is queued; a success message can mean the request was accepted rather than already delivered.

Coupons redeem once. QR verification alone does not redeem one. A voided/expired/redeemed coupon must not be treated as available to sell or exported as an active usable coupon. Ask an administrator to investigate an unexpected status instead of generating duplicate replacements casually.

### 6.13 Reports and unavailable menus

Use Sales and Variance Analysis to inspect variance composition and its detailed source register. Use Expense and Credit Reports for expense classification, cash taken from sales and credit sales. Use Monthly Movement Reports for product opening/closing stock, receipts, sales and loss/gain over the selected period. Apply filters before exporting CSV/PDF.

Payment Channel Setup, Export Data, Station Daily Pack and the OMC Audit and System Logs menu are currently commented out. They are not standard available menu instructions in this edition. Payment Method Setup remains available and is a different feature.

## 7 Station manager

Work only within the OMC and station assigned to your active manager account. Your station is supplied from station staff assignment; do not select another station to create operational records.

### 7.1 Read the dashboard

Monthly KPI cards show revenue and transaction counts; active attendants are counted from current station assignments rather than a monthly period. The weekly fuel-sales chart covers the previous week. Recent Transactions displays current-day station transactions with precise time and payment status. It is the live component; other dashboard analytics should not be assumed to stream continuously. Top-performing attendants are ranked for the month, prioritising transaction value.

Open total revenue/transaction-count drawers to inspect payment-method composition. Open Active Attendants to inspect assigned active pump attendants. If the station or staff is missing, ask your OMC admin to check station assignment and account status.

### 7.2 Create a shift template

Open Shifts Management > Create Template.

1. Enter the template name and verify the read-only station/manager.
2. Select the operating days. None are selected by default.
3. Select pumps for this template. None are selected by default. Only active station pumps with at least one active, non-deleted nozzle should be offered.
4. Enter the minimum required attendant headcount, date range, start/end time, status and optional notes.
5. Select Next: Assign Pumps.
6. Add an active attendant assigned to your station, then select the pumps that person covers. One attendant can cover multiple pumps; each pump has one accountable attendant in the template.
7. Repeat for other attendants. Reassign or remove a selection if coverage is wrong.
8. Save Template and confirm the saved record in Manage Templates.

An active template requires all selected pumps to be covered and the minimum distinct-attendant headcount to be met. Overlapping assignments can be rejected. A draft can be completed later. Use schedule times in the configured station/application timezone and confirm with the administrator if the browser time differs.

### 7.3 Edit suspend or reactivate a template

Open Manage Templates. Active templates appear as cards; the table includes other statuses such as Draft, Suspended and Expired.

Use Edit Template on an eligible unexpired record. Change days, schedule, pumps, required headcount, notes and assignments through the two-step form. Template name and station remain read only. Removing or reassigning an attendant affects current coverage; it does not erase historical transactions. Save Changes and inspect the updated assignments.

Use Suspend Template with a reason when a current template should no longer permit operation. Expired templates use Reactivate Template: provide valid dates/days/times and the confirmation requested. Past reactivation dates or already-elapsed end times are rejected. An attendant needs a valid active template matching the current day/date/time to access the selling context.

### 7.4 Record tank and pump readings

Open Sales > Meter Readings. Prepare actual physical measurements and the pump/nozzle counters. Do not enter a guessed measurement to clear a warning.

1. Choose Reading Type and Reading Date. The page supports Opening, Closing, Shift Handover, Pre Delivery, Post Delivery, Rainfall Check and Manual Audit; corrections are handled through the edit/correction workflow.
2. Shift Reference appears for shift-related readings. Select the eligible template rather than typing a free-text code.
3. Delivery Reference appears for delivery readings. Choose the relevant dispatched/received delivery associated with the tank.
4. Open the appropriate tank card to record its measurements. General opening/closing readings are station measurements rather than arbitrary shift references.
5. Enter tank dip/physical volume using the configured input mode, water volume in litres and return-to-tank volume where applicable.
6. Enter temperature only as the station policy requires. Record Only does not mean a correction factor was applied. Do not invent a VCF when measurement/correction is not configured.
7. Enter the required pump/nozzle counter readings linked to this tank. Opening readings establish both stock and available counter baselines.
8. Review the calculated preview, including expected/physical stock and variance, then submit once.
9. Repeat as needed for other tank cards and verify the saved entries in Reading History.

Water reduces net fuel volume. Record RTT only for a documented measured return using the designated field; do not enter the same return twice. A successful product receipt already updates operational tank stock. Pre/post-delivery readings provide physical evidence and must not be used to add the same delivery quantity again.

In Reading History, filter by date range, status and product. Use View Reading for inspection or Edit Reading for an eligible correction. Supply a reason and evidence where requested. A reading is not deleted to conceal an error. The manager reviews the table status; checker decisions are handled at OMC level.

Use Export CSV for the reading columns, or PDF/Print for the landscape reading report. Apply the desired period before exporting and keep the document as evidence of the recorded values, not proof that an unmeasured tank was physically checked.

### 7.5 Request stock

Open Stock Requisition. The server provides the request number and current request date.

1. Select the receiving tank/product offered for this station.
2. Read its capacity, current stock and available receiving space.
3. Enter the requested litres within the allowed receiving space.
4. Set a future/today ETA, priority and remarks.
5. Submit and verify the request in Requisition History.

Past ETA dates are disabled. Pending quantities and capacity policy can restrict an otherwise plausible request; use the server's message and contact the OMC reviewer rather than repeatedly increasing the quantity. Use View Requisition Details or Print Requisition for supporting evidence.

### 7.6 Receive dispatched fuel

Open Product Receipts and locate the relevant dispatched requisition/delivery.

1. Select Receive Product from the eligible row menu.
2. Verify request, station, receiving tank, product and dispatch/waybill details.
3. Enter the actual quantity received and complete the displayed receiving details/evidence.
4. Review shortage/overage and enter the required explanatory notes.
5. Submit once, then confirm the receipt and remaining/requisition status.
6. Check the tank's operational stock and record delivery dip evidence where the reading procedure requires it.

Do not mark a dispatch received without measuring/confirming the actual receipt. A partial receipt is different from a fully received delivery. Use the row print action for a single receipt and report exports for a filtered history. Receipt difference concerns that delivery; daily stock variance concerns the complete stock reconciliation.

### 7.7 Record expenses and banking deposits

Open Sales and Cash Summary and select the appropriate business date; future dates are disabled.

For an expense, select Add Expense. Choose an active OMC expense category, enter description, total amount and the optional amount taken directly from sales. Attach the receipt and add notes. Save once and confirm the expense status. A review-required expense stays pending; a no-approval category can auto-approve it with the recorded policy explanation.

For a deposit, select Banking Deposit. Enter business date, deposit date/time, bank, optional branch, slip/reference number, amount, uploaded slip and notes. Review the upload preview/attachment and submit. Confirm the recorded slip and status. This is a separate record; do not replace the evidence with a reconciliation-only number.

### 7.8 Reconcile cash and collections

Select Cash Reconciliation from Sales and Cash Summary.

1. Check the business date and expected collection breakdown.
2. Count physical cash and compare banking deposits with the day's recorded slips.
3. Enter actual POS, mobile-money, card, coupon and other displayed channel balances in their matching fields.
4. Enter notes for a shortage, surplus or unresolved provider item.
5. Save and inspect the new current reconciliation.

Each submission is retained as history while one current/latest record supplies the current summary. Expected collections stay gross; expenses taken from sales appear as deductions. Match each amount to its destination and avoid counting banked cash again as physical cash. Credit/card/coupon entries are not automatically cash in the drawer.

Read Cash Difference as balanced at zero, surplus when positive and shortage when negative. Inspect breakdowns before investigating. Use the date/product filters for Fuel Sales Summary and the main export control for that business day's summary.

### 7.9 Transactions stock analysis and stock variance

Open Transactions to inspect this station's transaction register. Search/filter by the offered criteria and use the 20-per-page carets. Open KPI drawers for payment-method count and value composition. Pending or failed rows do not count as successful revenue.

Use Sales Analysis for product/date trends and detailed sales. Read average realised price separately from a historical/current configured price. Use Stock Analysis for movement over a period. Use Stock Variance to inspect physical-versus-expected stock and evidence. Supply a correction request/evidence through eligible actions when a record needs attention; OMC decisions are not the manager's approval task.

If physical stock has no qualifying reading, do not substitute the tank's current system balance. Check which measurement/date the display is using and ask for a review if the source is missing.

### 7.10 Generate reports

Open Reports. Report Details offers Daily Sales, Shift Summary, Pump Activity and Fuel Consumption. Use View to open the table, then the offered CSV/PDF controls. Pump activity should be assessed using its sales and associated transaction details, not just the number of configured pumps.

For Custom Reports:

1. Select Meter Readings, Transactions, Pump Activity, Attendants or Expenses as the data source.
2. Select the date range.
3. Set the fields available for that source. Transaction reports include product, payment method and status. Attendant reports include assigned pump, shift template, minimum transaction count and minimum amount.
4. Choose Table, Chart or Both and select an offered chart type where relevant.
5. Generate Report, inspect the preview and export its data.
6. Use Reset to clear the report-builder fields before another report.

Transaction analysis compares transaction count with total amount, not merely paid count against all count. Operational fuel reports generally use product codes; customer receipts use product names. If a visible builder control does not alter results in your deployment, verify the output and report that control rather than treating it as an applied filter.

### 7.11 Submit EOD

EOD is the station's end-of-day submission to OMC review. It packages a business day's figures and manager checks; it is not the same as a retail till closure.

1. Set your EOD PIN in Manager Settings > Notifications and Security before the first submission.
2. Open EOD and choose the business date. Check station name and generated EOD reference.
3. Wait for the draft, then inspect sales, collections, expenses, deposits, stock and variance sections.
4. Use Refresh Draft after relevant source records change. Do not submit an outdated draft.
5. Review system checks. Fix real blockers through the relevant operational page.
6. Perform the manual checks yourself, toggle only completed checks and select Save Checklist.
7. Select Review and Submit EOD. Add manager notes and, for a past business day, the required late-submission reason.
8. Enter your six-digit EOD PIN and submit once.
9. Confirm the submitted state/reference and review history. The OMC checks the submission afterwards.

Shift templates do not require a shift-session closure to submit EOD. An unresolved OMC stock-variance review is a warning rather than an automatic manager blocker. Manual checklist answers do not override failed system checks. A PIN does not replace the need for accurate supporting records.

If the screen reports No EOD PIN Set, open Manager Settings as directed, configure the PIN and return to EOD. For an interrupted/late day, submit the actual previous business date with a reason rather than mixing its data into today's submission. Current EOD Print / PDF uses the browser print dialog.

## 8 Pump attendant mobile workflow

The pump attendant uses an external mobile app connected to the Easy Fuel attendant APIs. Screen labels can vary by mobile-app release; this section describes the verified backend workflow, not an invented mobile interface.

### 8.1 Before selling and login

Obtain your Ghana Card number and private six-digit attendant ID. Your account, station assignment and shift template must be active. The template must apply to the current date, weekday and time, and assigned pumps need usable active nozzles, tanks and products.

Sign in through the mobile app using Ghana Card and attendant ID. Check the returned station, template and assigned pumps. One attendant may have several assigned pumps. If access is refused, contact the manager to review schedule/assignment rather than using another attendant's credentials.

The attendant ID is a login secret, not an ordinary public staff reference. An OMC admin can resend it by SMS. Do not reveal it to a customer. Web login credentials and mobile attendant credentials are separate workflows.

### 8.2 Common sale preparation

1. Select the assigned pump/nozzle appropriate for the sale.
2. Confirm the product name and the accepted payment method.
3. Enter the requested amount for amount-based payments. The backend uses the effective price to derive litres.
4. Review the customer/payment details and submit once.
5. Keep the transaction reference until a final result is known.

The app should retain one sale attempt's reference/idempotency identity when retrying an interrupted request. As a user, check existing status before initiating another charge. Do not manually calculate litres for an amount-based sale. The litre input is used only when the verified card type requires litres.

### 8.3 Mobile money

Enter the customer's wallet phone number and supported issuer. Perform the app's name enquiry and verify the returned account name with the customer. Laravel handles provider authentication; attendants do not manually obtain or paste People's Pay tokens.

Enter the amount and initiate collection. The initial response means the payment was started; it is not proof the customer paid. Ask the customer to approve the provider prompt and wait while the app checks the stored transaction status. Only a successful paid result confirms receipt. If the customer claims to have paid while the app remains pending, check the same reference and escalate it; do not make another debit casually.

For a failed payment, read the provider/user message and use an appropriate supported retry/new-sale flow after confirming the original result. A missing connection or timeout alone must not be interpreted as a completed payment or a final failure.

### 8.4 Cash card and coupon sales

For Cash, enter the amount received for the sale and submit through the cash action. A valid accepted cash posting completes directly; there is no provider approval prompt. Physically collect the cash before recording it.

For Fuel Card, scan its QR or enter the card reference and validate it. The response identifies Currency or Litres input, status, balance and available attempts. Enter amount for a currency card or litres for a litre card. The backend validates balance/limit and applies the effective product price. Confirm the resulting amount/status. Card attempts are capped; inspect the remaining-attempt warning rather than repeatedly guessing. Administrative card attempt/reset policy is handled on the server.

For Fuel Coupon, scan the QR or enter the coupon code and validate it. A QR verification token is part of the coupon verification link, not your attendant access token. Validate eligibility and follow the returned coupon data to submit the coupon sale. A successful redemption changes the coupon to redeemed once. Do not accept an already redeemed, voided or expired coupon, and do not assume a public verification page completes redemption.

### 8.5 History and receipts

Use today's transaction-history view to inspect amount, payment method, product name, date/time and status for your own sales. The successful-amount total excludes pending and failed payments.

Open/download the available receipt after processing. Receipts are prepared for POS-style printing with OMC identity, transaction ID/reference, amount, status, date, product name and applicable customer/provider information. They do not show litres sold. A queued receipt may become available after processing; avoid creating another transaction merely to obtain a receipt.

## 9 Station supervisor

**Prototype.** The dedicated supervisor workspace presently uses sample records and local forms rather than the connected manager APIs. Its pills are Dashboard, Shift Templates, Meter Readings, Station Expenses, Cash Reconciliation and EOD. A live-looking label in this workspace is not proof of a live backend connection.

Use the tabs to review the proposed delegated station workflow. Shift Templates demonstrates pump-attendant assignment. Meter Readings demonstrates measurement entry/review. Station Expenses demonstrates category, amount, notes and evidence upload. Cash Reconciliation demonstrates expected-versus-actual entries. EOD demonstrates review and PIN-based submission controls.

The intended delegated responsibility is to assist the assigned station manager. A supervisor should not approve their own expenses, set network-wide prices, create OMCs or gain unrestricted cross-station analysis. Current prototype confirmations do not prove submission or approval. For production work, use an account/workflow authorised and connected by the administrator; section 7 provides the operational process, but those permissions are not automatically inherited by the prototype.

## 10 OMC operations administrator

**Prototype.** The dedicated header-tab workspace offers Overview, Stations, Tanks and Pumps and Nozzles. Its present forms and registers contain demonstration data.

Use Stations to practise a metadata-only setup: identity, owner, location, licensing, status and operational settings. This differs from the OMC admin's six-step station wizard. Use Tanks to practise selecting station/product and entering tank capacity/stock/threshold fields. Use Pumps and Nozzles to practise selecting a station, defining a pump and linking each nozzle to a tank.

The portal's intended scope is station metadata and tank/pump/nozzle connections. It does not grant payment integration, financial approval or full tenant administration. Do not treat prototype Save or Submit controls as persisted station configuration. Connected OMC admin master-data procedures are in section 6; the backend may authorise some operations roles for specific master-data APIs, but that does not make the dedicated prototype forms connected.

## 11 Audit risk and compliance

**Prototype.** The current tabs are Overview, Logs, Variances, Approvals, EOD and Reports. Tables and KPI figures in this dedicated workspace are sample data. Filter/export/comment controls are not all connected.

Use Logs to understand the proposed actor/module/time/action register. Use Variances to compare source, product, expected/actual figures, risk and review status. Use Approvals to inspect decision chains. Use EOD to review business-day submissions. Use Reports for proposed station/component comparisons. Assurance Notes demonstrates comments; do not assume a typed note was stored unless an actual save result and record confirms it.

The audit role is read only for operations. It should not change sales, approve a maker's expense, alter a variance outcome or edit station stock. A live review must rely on authorised connected reports and evidence exports until this portal is integrated. Read only auditor accounts follow the same caution with their narrower permissions.

## 12 Shop attendant POS and inventory

**Prototype.** The retail workspace uses in-memory data. Adding items, creating categories and completing a sale change local state while the portal remains mounted. Reloading, signing out or leaving/remounting the workspace can reset it. This is not yet a persistent retail inventory or payment ledger. Fuel transactions and card/coupon APIs are separate and must not be assumed to fund a retail checkout.

The shop attendant has no sidebar. Header tabs are Sell, Held Sales, Inventory, Sales History, Cash Drawer and My Shifts. The header shows shop/register identity and an account menu. Register Open is currently demonstration state; its pulsing indicator does not confirm hardware or a real open register session.

### 12.1 Review items before a sale

Open Sell. Wait for the skeleton to finish; item images are loaded before the grid is revealed, with a fallback for missing/failed images. Search by item name, SKU or barcode, or choose a category pill.

Each tile has a centered product image, small SKU/item-code lines, name, available quantity and price. Long identifiers can be viewed by hovering or opening the preview. The top-right eye button is subdued until hover/focus. Select it to open Item Details without adding the item to the basket. Review image, SKU, code, barcode, category, price, stock, reserved units and status. Use Close/Escape to dismiss or Add to Sale to add an eligible item.

Items without uploaded photographs show No image. This is not a category icon or a substitute product photograph. Check identity by name/SKU/barcode when an image is missing.

### 12.2 Add an inventory item and category

Open Inventory and select Add Item.

1. Choose Upload Image and select JPG/JPEG, PNG or WebP up to 2 MB. Inspect the preview. Replace Image or the remove icon changes the unsaved photo.
2. Enter Item Name and Item Code.
3. Choose Category. If necessary, select the small Create Category control next to its label, enter a new category name and Create. The category is selected automatically.
4. Enter optional subcategory, unique SKU and sales price in GHS.
5. Enter or scan the barcode. Keep the scanned value as the identifier; do not discard leading zeros.
6. Enter Opening Quantity and Reorder Level as whole numbers of zero or more.
7. Select Add Item and confirm the item appears in Inventory and Sell.

Duplicate item codes, SKUs and barcodes are rejected in the prototype form. Categories are records, not a fixed backend enum; the UI prototype carries OMC and station scope. Backend tenant/station enforcement and upload storage are still pending integration. Category and item changes do not survive a full reload.

The current form creates a new master item with its opening quantity. It is not a stock receipt/restock form for an existing item. Do not create duplicate item records to replenish an existing SKU; a persistent stock-receiving workflow is part of the planned backend work. CSV bulk item import is also not currently available in this shop UI.

### 12.3 Barcode scanning

The current barcode input supports a USB/Bluetooth scanner operating as a keyboard. Camera-based scanning is not implemented.

When creating an item, select Scan Barcode to focus the barcode field, then scan. A scanner normally types the code and sends Enter. The form captures the code without prematurely submitting the entire item. You can type the barcode manually if a reader is unavailable.

At Sell, focus Scan Barcode and scan an item. An exact matching barcode or supported SKU adds one unit and clears the scan field. An unknown code shows Item Not Found. Verify the barcode on the inventory item rather than repeatedly scanning a different label. Search by name if the barcode cannot be read.

### 12.4 Build a basket and complete a demonstration sale

1. Select an item tile to add one unit. Repeated clicks increase quantity; a double-click produces its normal two clicks, not a separate third addition.
2. Use plus/minus beside a basket line to change quantity. The cross removes the line; Clear Sale removes the basket.
3. Check each price, quantity, subtotal and total. Displayed amounts use GHS with two decimal places.
4. Select Pay to open Complete Sale.
5. Choose Cash, Mobile Money, POS or Fuel Card from the prototype choices.
6. For Cash, enter cash received. The form shows change and rejects a received amount below the total.
7. Select Complete Sale. The in-memory available stock is checked, quantity is deducted locally and the basket clears.

Available quantity equals on-hand units minus reserved units. Out-of-stock items cannot be added. The displayed discount is currently zero; no discount-entry workflow is connected. Non-cash choices do not initiate a real People's Pay/card/terminal payment. A success toast in this prototype is not a bank/provider settlement, persistent sale record or tax receipt.

### 12.5 Held sales and sales history

Hold clears the current basket and increases a local held count. The Held Sales tab shows separate sample baskets. Its Resume action navigates to Sell but does not restore a newly held basket's actual lines; Void removes a sample locally. Therefore, do not rely on Hold/Resume for preserving a real customer's order yet.

Sales History shows demonstration records, not a persistent history of the sales just completed in Sell. Search by the offered reference/payment/status fields to review the layout. Print Shift Summary and receipt print buttons are not connected receipt printing in this prototype.

### 12.6 Cash drawer and retail shifts

Cash Drawer demonstrates opening cash, cash sales, pay-in/out and expected cash. Use Pay In / Out to practise entering movement type, amount and reason. Use Close Register to practise counting actual cash and entering handover notes. Current confirmation messages do not update a persistent drawer ledger, close a real session, or reconcile the header's Register Open state.

Open Drawer currently shows feedback; it does not actuate a printer-connected cash drawer. Full-screen and several print controls also remain unconnected. My Shifts displays sample assigned sessions, values and time remaining rather than a live retail shift scheduler.

For the future live workflow, verify starting float at opening, record each manual pay-in/out with a reason, count cash at closing and explain any difference. Do not sign off a real retail session using prototype totals.

## 13 Cashier and additional role accounts

The cashier route currently opens a placeholder dashboard. Cashier users can be created/assigned where supported by fuel-station staffing, but no separate completed cashier operating manual can be claimed for this portal. Do not substitute the shop attendant prototype for a cashier's authorised production workflow.

OMC Owner routes to the OMC workspace. Finance Officer uses the same base workspace with finance/report access controlled by their permission profile. Only perform a procedure in section 6 when its menu and backend action are authorised for your account; being routed to a shared portal is not blanket approval authority.

System Administrator, Security Administrator, Platform Operations, Database Administrator, QA Lead, Customer Success and Support Analyst labels are grouped into the system portal by frontend routing. Dedicated granular operating procedures are not independently verified for each alias. Follow only the actions your server account is authorised to perform. System-admin endpoints can reject non-system-admin roles even when a shared interface is visible. Do not bypass a denied request or share another user's credentials.

Read Only Auditor shares the audit workspace and must remain read only. OMC Operations Administrator and its alternate role label share the operations workspace. Role display names are human readable; machine role keys and security identifiers are not information to disclose to ordinary users.

## 14 Reading financial and stock figures

### 14.1 Payment sales and prices

Successful transaction revenue is the amount from paid/completed financial records. Initiated/pending/failed payments are separate states. A cash posting can complete immediately; MoMo completion depends on the provider result.

Average realised price per litre is the sum of qualifying transaction amounts divided by the sum of their litres, for the selected scope. It is a weighted average. It can differ from the latest configured price if the period includes multiple price versions. Example: 10 L sold at GHS 14.00 and 20 L at GHS 15.00 produce GHS 440.00 over 30 L, approximately GHS 14.667/L. Changing today's configured price must not rewrite those older sales.

RTT affects stock/meter reconciliation. It does not automatically refund a paid transaction or change the original sale amount. Use the documented correction/refund process for a real financial change; do not reduce revenue simply to match a dip.

### 14.2 Physical stock and variance

Physical stock comes from a qualifying measurement, not just a stored tank balance. In the supported reconciliation flow, net observed fuel is dip volume minus water volume. A configured correction factor can then standardise that volume; if correction is not enabled, do not assume a temperature-adjusted quantity.

Expected/book stock includes the opening basis, received deliveries and recorded movements, less measured sales/dispensing and with valid return-to-tank treatment. Variance is physical fuel minus expected fuel: negative indicates a shortage, positive a surplus, and zero a balanced quantity. In the current reading calculator, variance percentage uses book stock as its denominator, while the configured tolerance can be litres or percentage. A zero book-stock denominator is guarded by returning zero percentage; inspect the litre difference rather than interpreting that percentage as evidence of no loss.

A delivery shortfall is a receipt variance. A daily dip difference is a stock variance. A transaction-versus-meter difference is a sales/meter variance. Their values may be investigated together but should not be indiscriminately summed when they describe the same discrepancy.

Financial stock exposure applies the relevant recorded price basis to variance litres. Look at the source/date and price basis in the detailed register. A price-change windfall estimates stock value impact; it is not equivalent to leakage or verified realised profit.

### 14.3 Collections and deposits

Expected gross collections, sales-funded expense deductions, bank deposits and actual counted channels are separate components. Read the accounting breakdown rather than subtracting an expense from every KPI. Fuel cards/coupons are treated as credit-sale channels in relevant reports; they are not automatically physical cash received at the till.

An approved expense, a recorded deposit, a submitted reconciliation and an approved EOD are different records. Approval of one must not be assumed to complete the others.

## 15 Troubleshooting

| Symptom | Check and next action |
| --- | --- |
| Login is refused | Verify email/password, account status and assigned role. Pump attendants must use the mobile Ghana Card/attendant-ID flow. |
| OTP did not arrive | Check the registered address and spam folder. Wait for the resend timer and request once. Ask support to review queued mail if delivery still fails. |
| Reset link does not work | Use the latest link; an expired or used link needs a fresh administrator-issued link. |
| Access Restricted | Confirm station/OMC assignment and permissions with the administrator. Do not attempt another role's URL. |
| Station/pump/attendant missing | Check active status, station assignment and current template date/day/time. A pump with no active non-deleted nozzle is not eligible for shift selection. |
| Product/payment option missing | Ask the OMC admin to check active master data and the station's selected products/payment methods. |
| MoMo remains pending | Check the same transaction reference and customer's provider prompt. Escalate with reference/time; do not automatically create a second charge. |
| Card/coupon rejected | Inspect state, balance, limit, expiry/redemption and remaining attempts. Ask an authorised admin to investigate. |
| Capacity/request error | Compare requested/approved/dispatched quantities with the receiving tank and server's capacity policy. |
| Physical stock missing or zero | Check whether an eligible physical reading exists for the tank and period. A system stock balance is not a substitute measurement. |
| EOD reference or station never resolves | Refresh once, verify connectivity and active manager station assignment, then report the error. Do not submit another station's data. |
| EOD says no PIN | Configure the six-digit EOD PIN in manager security settings and return to the draft. |
| File upload fails | Check the specific form's allowed type/size. Tenant logo and retail item image limits differ. |
| Retail barcode not found | Confirm the exact barcode/SKU, active item and scanner focus. Add the missing item only if it is genuinely a new item. |
| Retail item/history disappeared | Prototype state resets on reload/remount and its history is sample data; this is not a durable retail ledger. |
| Page keeps showing skeleton | Confirm network connectivity; image loading has a fallback. Capture page/date/filter context if it never resolves. |
| Server unavailable message | Record page, action, time and business reference. System admin should inspect Error Logs. Do not paste credentials into a ticket. |

For a support request, include the role, station name, page, operation, business date, record reference, displayed status and exact user-facing error. A screenshot can help if it excludes sensitive fields. Retain original transaction references during retries.

## 16 Operating checklists and glossary

### 16.1 Station manager daily checklist

1. Confirm station assignment and the day's active templates, staff and usable pumps/nozzles.
2. Record opening tank/pump baselines and any required physical checks.
3. Track receipts and delivery evidence without double-counting stock.
4. Review pending/failed payments using their original references.
5. Record expenses and deposit slips with evidence.
6. Record closing readings and investigate differences with supporting notes.
7. Count actual collections and save the day's reconciliation.
8. Refresh EOD, complete manual checks and submit with the EOD PIN.

### 16.2 OMC reviewer checklist

1. Inspect pending requisitions, approve/decline with reasons and dispatch eligible stock.
2. Review receipt discrepancies and measured stock/cash variances.
3. Review expenses and deposits with evidence and maker/checker controls.
4. Review station EOD submissions and follow up on missing/late records.
5. Check scheduled prices and finance/report periods before exporting.
6. Confirm user/station/master-data activity and remove obsolete access through authorised controls.

### 16.3 Shop prototype review checklist

1. Add a distinct item with a real photo, valid category, SKU and barcode.
2. Find it by name/SKU and scan its barcode in Sell.
3. Preview its full details and add it to the basket.
4. Change quantity and verify that displayed totals remain legible.
5. Complete a demonstration cash sale and verify the local stock reduction.
6. Confirm the documented prototype limitations before approving a backend integration design.

### Glossary

| Term | Meaning |
| --- | --- |
| OMC | Oil Marketing Company; the tenant organisation. |
| Station assignment | Active link between a user and the station where they work. |
| Shift template | Reusable dates/days/times and pump-attendant coverage; not a shift session. |
| Nozzle | Dispensing point linked to a pump, tank and fuel product. |
| Dip | Physical tank measurement converted/entered using the configured reading mode. |
| RTT | Return to tank; a recorded fuel return included in reconciliation. |
| VCF | Volume correction factor used only when valid correction is configured. |
| Variance | Difference between an actual measurement/collection and its expected basis. |
| EOD | End-of-day station submission for a business date. |
| Maker checker | Separation between the person creating a review-required record and the person deciding it. |
| MoMo | Mobile-money collection through the configured provider. |
| SKU | Stock keeping unit identifying a retail item. |
| Barcode | Scannable retail item identifier; preserve the exact stored value. |
| Reserved stock | Units already reserved and unavailable for new sale selection. |
| Prototype | Demonstration UI/state that is not yet a durable production workflow. |

### Source and maintenance note

This edition was checked against the current frontend role routes/navigation, auth pages, station manager pages, OMC pages, system administration pages, shop inventory/POS components and backend attendant/payment routes. It intentionally identifies disabled menus, placeholders and sample-data workspaces. Update the manual after backend retail integration, delegated portal integration, permission changes or a deployment changes available controls. No production credentials or tenant-private records are included.
