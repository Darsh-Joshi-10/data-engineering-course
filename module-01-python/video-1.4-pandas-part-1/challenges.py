"""Video 1.4 homework — Pandas Fundamentals (Kaggle-inspired).

Run generate_data.py first so the files exist in data/raw/.
Run from the repo root: python exercises/04_pandas_part1_exercises.py
Do them, commit, and push. Solutions go up 24 hours after the video.
"""

from pathlib import Path
import pandas as pd

raw_dir = Path("data") / "raw"

# ---------------------------------------------------------------
# CHALLENGE 1: Reading and Basic Inspection
# Read "products.json" from data/raw/ into a DataFrame.
# Return a tuple of: (DataFrame shape, list of column names)
# ---------------------------------------------------------------
def inspect_products() -> tuple:
    # TODO
    pass


# ---------------------------------------------------------------
# CHALLENGE 2: Indexing, Selecting, and Assigning
# Read "orders_messy.csv", select only the "order_id", "customer_id", 
# and "amount" columns. Then create a new column "amount_with_tax" 
# which is amount * 1.05. Return the resulting DataFrame.
# ---------------------------------------------------------------
def add_tax_column() -> pd.DataFrame:
    # TODO
    pass


# ---------------------------------------------------------------
# CHALLENGE 3: Handling Missing Data & Grouping
# Read "orders_messy.csv", coerce the "amount" column to numeric 
# (turning bad strings/nulls into NaN), fill missing amounts with 0.0, 
# and group by "customer_id" to calculate total spend per customer.
# Return a DataFrame with columns: customer_id, total_spend.
# ---------------------------------------------------------------
def calculate_customer_spend() -> pd.DataFrame:
    # TODO
    pass


if __name__ == "__main__":
    print("--- Testing Challenge 1 ---")
    # shape, cols = inspect_products()
    # print(f"Shape: {shape}, Columns: {cols}")

    print("\n--- Testing Challenge 2 ---")
    # df_tax = add_tax_column()
    # print(df_tax.head(3))

    print("\n--- Testing Challenge 3 ---")
    # df_spend = calculate_customer_spend()
    # print(df_spend.head(3))