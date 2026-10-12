from pathlib import Path
import pandas as pd

raw = Path("data") / "raw"
clean = Path("data") / "clean"
clean.mkdir(parents=True, exist_ok=True)

print(pd.read_excel(raw / "report.xlsx", sheet_name="Orders"))

orders = pd.read_excel(raw / "report.xlsx", sheet_name="Orders", header=2)
print(orders)
print(orders.dtypes)

print(pd.to_datetime(orders["order_date"], errors="coerce"))


def parse_excel_date(value):
    """Handle real dates, text dates, and Excel serial numbers."""
    if isinstance(value, (int, float)) and not pd.isna(value):
        return pd.to_datetime(value, unit="D", origin="1899-12-30")
    return pd.to_datetime(value, errors="coerce")


orders["order_date"] = orders["order_date"].apply(parse_excel_date)
print(orders)

bad_dates = orders["order_date"].isna().sum()
print(f"Dates that could not be parsed: {bad_dates}")

sheets = pd.read_excel(raw / "report.xlsx", sheet_name=None)
print(list(sheets.keys()))

orders.to_csv(clean / "report_orders_clean.csv", index=False)
print("Done. Clean files are in", clean)