# Scholarship Dinners Seat Board

A live stats board for the **Scholarship Dinners – Seat Requests** Google Sheet: requests per event and brand, timeline, visa status, where guests live, how they heard about the dinners, traffic source, and ticketing and check-in progress. Same look as the Scorp outcomes dashboard.

- **Live page:** https://fahadasif1.github.io/scholarship-dinners-dashboard/
- **Repo:** https://github.com/fahadasif1/scholarship-dinners-dashboard (public, GitHub Pages from `main`, root)

## Using it

1. Open the live page. It loads the sheet straight away (no link to paste). If the sheet stops being link-readable the page shows a message and a *Try again* button.
2. Click an event card, a bar or a table row to filter; use the filter pills for more. Chips show what is applied.
3. **Copy view link** gives a URL that reopens the same filters for anyone who opens it. **Export CSV** downloads counts by brand and event. **Print** saves the page as PDF.
4. The page re-reads the sheet every two minutes, so new requests appear without a redeploy.

## Rules baked in

- **Two events were moved.** London was first listed for Thu 29 Oct and is now Fri 30 Oct; Birmingham was first listed for Mon 2 Nov and is now Thu 12 Nov. Every row counts on the final date whichever date the form said (`EVENT_DATE_FIX` at the top of the script in `index.html`). Each moved card notes how many signed up under the old date. When another event moves, add its city and new day to `EVENT_DATE_FIX`.
- **Flagged duplicates are left out** (Duplicate? = Yes) unless you tick *Include flagged duplicates*.
- Brand names that differ only by capitals or spacing are merged.
- The sheet is matched by column header (Submitted at, Brand, Event, Postcode (optional), Visa status, Heard about us, Marketing opt-in, utm_source, Ticket sent, Checked in (ID seen), Duplicate?, Page variant), so column order does not matter.

## Privacy

- The page reads a **stats-only sheet** (`DEFAULT_SHEET` in `index.html`): no names, phones, emails or postcodes, so it is safe for that sheet to be link-readable. The original sheet with contact details stays private.
- The browser reads the sheet straight from Google and keeps it in memory. Names, phone numbers and emails are never shown, exported or sent anywhere; only counts are.
- The stats-only sheet's ID is in the public repo, so anyone who finds it can read the rows in that sheet. Keep personal columns out of it. Google shares a whole spreadsheet, not single tabs, so never add contact details as another tab there.
- If the sheet has no `Postcode` column, the *Where they live* card and its filter are hidden.

## Develop

Single file, no build step, no dependencies.

```bash
python3 tests/make-fake-csv.py > fake.csv     # synthetic rows (fake.csv is git-ignored)
python3 -m http.server 8771                   # then in the browser console on http://localhost:8771/
                                              #   SeatBoard.show(await (await fetch("/fake.csv")).text())
git add -A && git commit -m "Describe the change" && git push   # Pages redeploys in 1-2 minutes
```
