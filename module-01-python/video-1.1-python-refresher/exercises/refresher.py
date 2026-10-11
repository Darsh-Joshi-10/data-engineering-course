"""Video 1.1 - Python Refresher: The DE 20%.

Type everything along with the video. Use the repo to check your work AFTER.
"""
from pathlib import Path

# ---------------------------------------------------------------
# PART 1: THE SYNTAX THAT MATTERS
# ---------------------------------------------------------------

# --- f-strings ---
rows_loaded = 1240
source = "sales_api"

print(f"Loaded {rows_loaded} rows from {source}")

# --- lists and dicts ---
columns = ["name", "email", "city"]
user = {"name": "Ada", "email": "ada@example.com", "city": "London"}

# --- list comprehension ---
raw_cities = ["  london ", "PARIS", "tokyo  "]

cities = [c.strip().lower() for c in raw_cities]
print(cities)

# --- enumerate ---
for i, city in enumerate(cities):
    print(f"{i}: {city}")

# --- zip ---
names = ["Ada", "Grace"]
emails = ["ada@x.com", "grace@x.com"]
for name, email in zip(names, emails):
    print(f"{name} -> {email}")


# --- functions: type hints + docstrings ---
def clean_city(raw: str) -> str:
    """Normalize a city name: strip whitespace, lowercase."""
    return raw.strip().lower()


print(clean_city("  BERLIN "))

# --- truthiness ---
rows = []
if rows:  # same as: if len(rows) > 0
    print("has data")
else:
    print("empty - skip the load")

missing_email = ""  # None or "" both count as missing
if not missing_email:
    print("flag this row")

# ---------------------------------------------------------------
# PART 2: THE DE-SPECIFIC TOOLBOX
# ---------------------------------------------------------------

# --- strings you'll use daily ---
raw = "  ORDER-2026-AB 124 "

print(raw.strip())           # "ORDER-2026-AB 124"
print(raw.split("-"))        # ["  ORDER", "2026", "AB 124 "]
print(raw.replace(" ", ""))  # "ORDER-2026-AB124"
print(raw.lower())           # "  order-2026-ab 124 "

# --- dicts, safely ---
user = {"name": "Ada"}

# city = user["city"]  # crashes with KeyError if the key is missing

city = user.get("city")             # returns None instead
city = user.get("city", "unknown")  # or a default
print(city)

# --- iterate dicts properly ---
for key, value in user.items():
    print(f"{key}: {value}")

# --- file paths without pain ---
data_dir = Path("data")
file_path = data_dir / "raw" / "users.csv"

print(file_path)  # data/raw/users.csv on every OS
file_path.parent.mkdir(parents=True, exist_ok=True)
