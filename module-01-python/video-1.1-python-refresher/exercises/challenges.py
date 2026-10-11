"""Video 1.1 homework - three small challenges.

Do them, commit, push. Solutions go up 24 hours after the video.
"""
from pathlib import Path

# ---------------------------------------------------------------
# CHALLENGE 1: List comprehension
# Clean this list: strip whitespace and uppercase every country code.
# Expected: ["IN", "US", "GB"]
# ---------------------------------------------------------------
raw_countries = [" in", "US ", " gb "]

countries = []  # TODO: replace with a list comprehension
print(countries)

# ---------------------------------------------------------------
# CHALLENGE 2: .get() safety fix
# This crashes on the second record. Fix it so missing phones
# become "unknown" instead of raising a KeyError.
# ---------------------------------------------------------------
records = [
    {"name": "Ada", "phone": "555-0100"},
    {"name": "Grace"},
]

for record in records:
    print(f"{record['name']}: {record['phone']}")  # TODO: fix with .get()

# ---------------------------------------------------------------
# CHALLENGE 3: pathlib
# Build the path data/processed/2026/sales.csv using Path and the /
# operator (no string concatenation), then create the parent folders
# only if they don't exist.
# ---------------------------------------------------------------
# TODO: build `output_path`, then create its parent folders
# print(output_path)
