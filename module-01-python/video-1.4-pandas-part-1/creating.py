import pandas as pd

df = pd.DataFrame({
    "products" : ["Laptop", "mouse", "keyboard"],
    "price" : [1200, 25, 75],
    "in_stock" : [True, True, False]
})

# print(df)
# prices = df["price"]
# prod1 = df.iloc[0]
# prod1 = df.loc[df["products"]=="Laptop"]
# print(prod1)

df["discounted_price"] = df["price"]*0.9
print(df)