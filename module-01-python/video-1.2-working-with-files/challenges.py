"""Video 1.2 homework - three small challenges.

Run generate_data.py first so the files exist in data/raw/.
Run from the repo root. Do them, commit, push. Solutions go up 24 hours after the video.
"""
from pathlib import Path

import pandas as pd

raw = Path("data") / "raw"
clean = Path("data") / "clean"
clean.mkdir(parents=True, exist_ok=True)

# ---------------------------------------------------------------
# CHALLENGE 1: CSV
# Read orders_messy.csv (skip the bad line), turn "amount" into numbers,
# drop the rows with no amount, and save the result to
# data/clean/orders_valid.csv (no index column).
# Expected: 4 rows left.
# ---------------------------------------------------------------
# TODO

# ---------------------------------------------------------------
# CHALLENGE 2: JSON
# Flatten users_nested.json and keep only name, email, and city.
# Users with no city should say "unknown".
# Expected: 5 rows, and exactly 1 user with city "unknown".
# ---------------------------------------------------------------
# TODO

# ---------------------------------------------------------------
# CHALLENGE 3: Excel
# Read the "Orders" sheet of report.xlsx (the header is on row 3), convert
# order_date to real dates, and count how many dates could not be parsed.
# Remember: errors="coerce" alone mishandles Excel serial numbers.
# Expected: 1
# ---------------------------------------------------------------
# TODO