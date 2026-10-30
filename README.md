# Scholarship Dinners Seat Board

A live stats board for the **Scholarship Dinners – Seat Requests** Google Sheet: requests per event and brand, timeline, visa status, where guests live, how they heard about the dinners, traffic source, ticketing and check-in progress, and data quality. Same look as the Scorp outcomes dashboard.

- **Live page:** https://fahadasif1.github.io/scholarship-dinners-dashboard/
- **Repo:** https://github.com/fahadasif1/scholarship-dinners-dashboard (public, GitHub Pages from `main`, root)

## Using it

1. Open the live page. It loads the sheet straight away (no link to paste). The sheet must be shared as **Anyone with the link can view**, otherwise the page shows a message and a *Try again* button.
2. Click an event card, a bar or a table row to filter; use the filter pills for more. Chips show what is applied.
3. **Copy view link** gives a URL that reopens the same filters for anyone who opens it. **Export CSV** downloads counts by brand and event. **Print** saves the page as PDF.
4. The page re-reads the sheet every two minutes, so new requests appear without a redeploy.

## Rules baked in

- **London is the 30 October event.** It was first listed for Thu 29 Oct and then moved. Every London row counts as 30 Oct whichever date the form said (`EVENT_DATE_FIX` at the top of the script in `index.html`). Rows that said the 29th are counted in the data-quality panel.
- **Flagged duplicates are left out** (Duplicate? = Yes) unless you tick *Include flagged duplicates*.
- Brand and counsellor names that differ only by capitals or spacing are merged.
- The sheet is matched by column header (Submitted at, Brand, Event, Postcode, Visa status, Heard about us, Marketing opt-in, utm_source, Ticket sent, Checked in (ID seen), Counsellor, Duplicate?, Page variant), so column order does not matter.

## Privacy

- The published page holds the **sheet ID** (`DEFAULT_SHEET` in `index.html`) and code. No names, no numbers.
- The browser reads the sheet straight from Google and keeps it in memory. Names, phone numbers and emails are never shown, exported or sent anywhere; only counts are.
- Because the sheet ID is in the public repo, **anyone who finds the repo can read the sheet** while it is link-shared, including the names, phones and emails in it (not just the board's counts). To avoid that, point `DEFAULT_SHEET` at a separate tab or sheet that holds only the non-personal columns.

## Develop

Single file, no build step, no dependencies.

```bash
python3 tests/make-fake-csv.py > fake.csv     # synthetic rows (fake.csv is git-ignored)
python3 -m http.server 8771                   # then in the browser console on http://localhost:8771/
                                              #   SeatBoard.show(await (await fetch("/fake.csv")).text())
git add -A && git commit -m "Describe the change" && git push   # Pages redeploys in 1-2 minutes
```
