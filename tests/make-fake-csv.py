"""Write a synthetic Seat requests CSV (fake names, same columns) for trying the board without the real sheet.

  python3 tests/make-fake-csv.py > fake.csv
"""
import csv, random, sys
from datetime import datetime, timedelta
random.seed(7)
H = ["Submitted at","Brand","Page variant","Page URL","Reference","Status","Duplicate?","Full name","Phone","Email","Postcode","Event","Visa status","Heard about us","Consent","Marketing opt-in","utm_source","utm_medium","utm_campaign","utm_content","utm_term","Ticket sent","Checked in (ID seen)","Notes","Counsellor"]
brands = [("Study Advisers","sauk-lahore"),("Study Icon","study-icon"),("Universal Study Advisors","usa"),("Students Club","students-club"),("Career Advisers","career-advisers"),("IAUK","iauk")]
events = ["London – Thursday 29 October 2026"]*2 + ["London – Friday 30 October 2026"]*5 + ["Manchester – Thursday 5 November 2026"]*3 + ["Birmingham – Monday 2 November 2026"]*2
pcs = ["M14 5QT","IG3 8QD","B26 2JN","E78DX","RM6 5QX","SM4 5HN","BL4 7HG","S9 1WZ","G42 8JH","HA0 4TW","", "ZZ"]
w = csv.writer(sys.stdout, lineterminator="\n"); w.writerow(H)
t0 = datetime(2026,10,23,16,0)
for i in range(400):
    b, v = random.choice(brands); t = t0 + timedelta(hours=random.random()*170)
    w.writerow([t.strftime("%m/%d/%Y %H:%M:%S").lstrip("0").replace("/0","/"), b, v, "", f"REF-{i}", "Pending", random.choice(["","","","","","","","Yes"]), f"Fake Person {i}", "07000000000", f"fake{i}@example.com", random.choice(pcs), random.choice(events), random.choice(["Graduate visa"]*4+["Student visa"]*2+["Other"]), random.choice(["Facebook","Instagram","WhatsApp","Friend or referral","Other"]), "yes", random.choice(["yes","yes","yes","no"]), random.choice(["","","","sendfox","ig"]), "", "", "", "", "TRUE" if i % 40 == 0 else "FALSE", "FALSE", "", random.choice(["","","","","Moiz Imran","moiz imran","Dr Rubab"])])
