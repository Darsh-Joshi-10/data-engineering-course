import pandas as pd

df = pd.DataFrame({
    "products" : ["Laptop", "mouse", "keyboard"],
    "price" : [1200, 25, 75],
    "in_stock" : [True, True, False]
})

# print(df.describe())
# print(df["products"].unique())
# print(df["products"].value_counts())

stock_status = df["in_stock"].map({True : "Available", False : "Out of Stock"})
print(stock_status)