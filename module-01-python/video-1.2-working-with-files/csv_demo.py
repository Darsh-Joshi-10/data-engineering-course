from pathlib import Path

import pandas as pd

raw = Path("data") / "raw"
clean = Path("data") / "clean"
clean.mkdir(parents=True, exist_ok=True)

df = pd.read_csv(raw / "orders_messy.csv", on_bad_lines="warn")
print(f"Read {len(df)} rows")

df.info()                    

blank_before = df["amount"].isna().sum()   

df["amount"] = pd.to_numeric(df["amount"], errors="coerce")
df.info()                     

blank_after = df["amount"].isna().sum()
print(f"Values that coerce turned into NaN: {blank_after - blank_before}") 

df.to_csv(clean / "orders_clean.csv", index=False)   