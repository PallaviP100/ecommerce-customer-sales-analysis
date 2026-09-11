import pandas as pd
import numpy as np

df = pd.read_csv("Superstore_data.csv", encoding='latin1')

print(df.head())
print("===Rows -columns===")
print(df.shape)
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])

print("===data types and columns===")
print(df.info())
print("====================")


print(df.describe())


print("Mising values")
print(df.isnull().sum())

df.dropna(inplace=True)


print("Duplicate records-")
print(df.duplicated().sum())
df.drop_duplicates(inplace=True)

print("Data types")
print(df.dtypes)

df["Order Date"] = pd.to_datetime(df["Order Date"])

df["Ship Date"] = pd.to_datetime(df["Ship Date"])

print("------------------------")
print(df.dtypes)


print("New features adding")

df["Order Year"] = df["Order Date"].dt.year

df["Order Month"] = df["Order Date"].dt.month_name()

df["Month Number"] = df["Order Date"].dt.month

df["Order Value"] = (
    df.groupby("Order ID")["Sales"]
      .transform("sum")
)


df["Delivery Time"] = (
    df["Ship Date"] - df["Order Date"]
).dt.days

df["Customer Lifetime Value"] = (
    df.groupby("Customer ID")["Sales"]
      .transform("sum")
)

print("=========New features added====================")
print(df[[
    "Order Date",
    "Order Month",
    "Month Number",
    "Order Year",
    "Order Value",
    "Delivery Time",
    "Customer Lifetime Value"
]].head())


# New cleaned file creation
df.to_csv("Superstore_Cleaneddata.csv", index=False)

