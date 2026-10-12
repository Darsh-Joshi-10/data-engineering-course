import json
from pathlib import Path
import pandas as pd

raw = Path("data") / "raw"
clean = Path("data") / "clean"
clean.mkdir(parents=True, exist_ok=True)

with open(raw / "users_nested.json", encoding="utf-8") as f:
    users = json.load(f)

users_df = pd.json_normalize(users, sep="_")
users_df = users_df.rename(columns={"address_city" : "city", "address_zip" : "zip"})
users_df["city"] = users_df["city"].fillna("unknown")
print(pd.DataFrame(users_df))

users_df.to_json(clean / "users_flat.json", orient="records", indent=2)