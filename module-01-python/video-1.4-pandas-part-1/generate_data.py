"""Generate raw data CSV and JSON files for Video 1.4 (Pandas Part 1).

Run from the repo root:
python module-01-python/04_pandas/generate_data.py
"""

from pathlib import Path
import pandas as pd
import json

def generate_files():
    # Ensure raw data directory exists
    raw_dir = Path("data") / "raw"
    raw_dir.mkdir(parents=True, exist_ok=True)

    # ---------------------------------------------------------
    # 1. Generate orders_messy.csv
    # Contains missing values, bad strings, and mixed dtypes
    # ---------------------------------------------------------
    csv_path = raw_dir / "orders_messy.csv"
    csv_data = """order_id,customer_id,amount,order_date,status
101,501,120.50,2026-10-01,COMPLETED
102,502,45.00,2026-10-01,PENDING
103,501,BAD_DATA,2026-10-02,COMPLETED
104,503,,2026-10-02,CANCELLED
105,504,300.25,2026-10-03,COMPLETED
106,502,75.50,2026-10-03,COMPLETED
107,505,150.00,,PENDING
108,501,220.00,2026-10-04,COMPLETED
"""
    csv_path.write_text(csv_data)
    print(f"Generated: {csv_path}")

    # ---------------------------------------------------------
    # 2. Generate products.json
    # Simple JSON dataset for DataFrame construction & mapping practice
    # ---------------------------------------------------------
    json_path = raw_dir / "products.json"
    products_data = [
        {"product": "Laptop", "price": 1200.0, "in_stock": True},
        {"product": "Mouse", "price": 25.0, "in_stock": True},
        {"product": "Keyboard", "price": 75.0, "in_stock": False},
        {"product": "Monitor", "price": 300.0, "in_stock": True},
        {"product": "Headphones", "price": 80.0, "in_stock": False}
    ]
    json_path.write_text(json.dumps(products_data, indent=2))
    print(f"Generated: {json_path}")

if __name__ == "__main__":
    generate_files()
    print("All practice data successfully generated!")