"""Generates intentionally messy sample files for Video 1.2.

Run from the repo root:
    python module-01-python/video-1.2-working-with-files/generate_data.py

Creates, inside data/raw/ (which is gitignored):
    orders_messy.csv   - a blank amount, a blank city, a text amount, one broken row
    users_nested.json  - nested addresses, one user with a missing zip, one with no address
    report.xlsx        - title above the header, dates stored three different ways
"""
from datetime import datetime
from pathlib import Path

import json
from openpyxl import Workbook

raw_dir = Path("data") / "raw"
raw_dir.mkdir(parents=True, exist_ok=True)

# ---------------------------------------------------------------
# orders_messy.csv
# ---------------------------------------------------------------
orders_csv = """order_id,customer,city,amount
1001,Ada,London,129.99
1002,Grace,Paris,
1003,Linus,,45.50
1004,Alan,Manchester,not_a_number
1005,Katherine,Houston,89.00,EXTRA
1006,Dennis,New York,230.25
1007,Barbara,Boston,15.75
"""
with open(raw_dir / "orders_messy.csv", "w", encoding="utf-8") as f:
    f.write(orders_csv)

# ---------------------------------------------------------------
# users_nested.json
# ---------------------------------------------------------------
users = [
    {"id": 1, "name": "Ada Lovelace", "email": "ada@example.com",
     "address": {"city": "London", "zip": "EC1A"}},
    {"id": 2, "name": "Grace Hopper", "email": "grace@example.com",
     "address": {"city": "New York", "zip": "10001"}},
    {"id": 3, "name": "Linus T", "email": "linus@example.com",
     "address": {"city": "Paris"}},
    {"id": 4, "name": "Alan Turing", "email": "alan@example.com"},
    {"id": 5, "name": "Margaret H", "email": "margaret@example.com",
     "address": {"city": "Boston", "zip": "02108"}},
]
with open(raw_dir / "users_nested.json", "w", encoding="utf-8") as f:
    json.dump(users, f, indent=2)

# ---------------------------------------------------------------
# report.xlsx  (title, blank row, header on row 3, dates stored 3 ways)
# ---------------------------------------------------------------
wb = Workbook()
ws = wb.active
ws.title = "Orders"
ws.append(["Orders Report - Finance Team"])
ws.append([])
ws.append(["order_id", "order_date", "amount"])
ws.append([1001, datetime(2026, 1, 5), 129.99])   # a real date
ws.append([1002, datetime(2026, 1, 6), 45.50])    # a real date
ws.append([1003, "2026-01-07", 89.00])            # a date typed as text
ws.append([1004, 46030, 230.25])                  # an Excel serial number (2026-01-08)
ws.append([1005, "not a date", 15.75])            # garbage

notes = wb.create_sheet("Notes")
notes.append(["Dates in this report were typed by hand, so formats are mixed."])
wb.save(raw_dir / "report.xlsx")

print(f"Sample files written to {raw_dir}/")