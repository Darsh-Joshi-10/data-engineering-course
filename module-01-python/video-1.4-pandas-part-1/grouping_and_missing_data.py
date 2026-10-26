import pandas as pd

df = pd.read_csv("data/raw/orders_messy.csv")

# print(df.isna().sum())

df["amount"] = pd.to_numeric(df["amount"], errors = "coerce")

df["amount"] = df["amount"].fillna(0.0)
df["status"] = df["status"].fillna("UNKNOWN")

# print(df.info())

customer_summary = df.groupby("customer_id").agg(
    total_spend = ("amount", "sum"),
    order_count = ("order_id", "count")
).reset_index()

print(customer_summary)