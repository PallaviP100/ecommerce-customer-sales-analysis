import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split


from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)


df = pd.read_csv("Superstore_Cleaneddata.csv")

print("Rows:", df.shape[0])
print("Columns:", df.shape[1])

df["Order Date"] = pd.to_datetime(df["Order Date"])

df["Ship Date"] = pd.to_datetime(df["Ship Date"])

print("------------------------")
print(df.dtypes)


print(df.info())
print("===================")
print(df.describe())



#
# # MISSING VALUE ANALYSIS
# print("Missing values analysis")
# print(df.isnull().sum())
# print("=======================")
#
# # Distribution of sales
#
# plt.figure(figsize=(8,5))
#
# plt.hist(df["Sales"], bins=30)
#
# plt.title("Distribution of Sales")
# plt.xlabel("Sales")
# plt.ylabel("Frequency")
#
# plt.show()
#
#
# # Category analysis
#
# # Sales by Category
# category_sales = df.groupby("Category")["Sales"].sum().sort_values()
#
# category_sales.plot(kind="bar", figsize=(7,5))
#
# plt.title("Sales by Category")
# plt.ylabel("Sales")
#
# plt.show()
#
# # Profit by Category
# category_profit = df.groupby("Category")["Profit"].sum()
#
# category_profit.plot(kind="bar")
#
# plt.title("Profit by Category")
#
# plt.show()
#
#
#
# # Customer analysis
#
# # Top 10 customers
# top_customers = (
#     df.groupby("Customer Name")["Sales"]
#       .sum()
#       .sort_values(ascending=False)
#       .head(10)
# )
#
# top_customers.plot(kind="bar")
#
# plt.title("Top 10 Customers")
#
# plt.show()
#
# # Repeat customers
# repeat = (
#     df.groupby("Customer ID")["Order ID"]
#       .nunique()
# )
#
# print("Count of Repeated customers")
# print(repeat[repeat > 1].count())
#
#
#
# # Geographic analysis
#
# # Sales by state
# state_sales = (
#     df.groupby("State")["Sales"]
#       .sum()
#       .sort_values(ascending=False)
#       .head(10)
# )
#
# state_sales.plot(kind="bar")
#
# plt.title("Top States by Sales")
#
# plt.show()
#
# # Sales by region
# region = df.groupby("Region")["Sales"].sum()
#
# region.plot(kind="bar")
#
# plt.title("Sales by Region")
#
# plt.show()
#
#
#
# # Time-series analysis
#
#
# # Monthly sales
# monthly_sales = (
#     df.groupby(["Order Year","Order Month"])["Sales"]
#       .sum()
# )
#
# monthly_sales.plot(figsize=(12,5))
#
# plt.title("Monthly Sales Trend")
#
# plt.show()
#
# # Yearly sales trend
# yearly = df.groupby("Order Year")["Sales"].sum()
#
# yearly.plot(kind="line", marker="o")
#
# plt.title("Yearly Sales")
#
# plt.show()
#
#
# # Correlation analysis
#
# numeric = df.select_dtypes(include="number")
# corr = numeric.corr()
#
# plt.figure(figsize=(8,6))
#
# plt.imshow(corr, aspect="auto")
#
# plt.xticks(range(len(corr.columns)), corr.columns, rotation=90)
# plt.yticks(range(len(corr.columns)), corr.columns)
#
# plt.colorbar()
#
# plt.title("Correlation Heatmap")
#
# plt.show()
#
#
# # Outlier detection
#
# # sales
# plt.figure(figsize=(6,4))
#
# plt.boxplot(df["Sales"])
#
# plt.title("Sales Outliers")
#
# plt.show()
#
# # Profit
# plt.figure(figsize=(6,4))
#
# plt.boxplot(df["Profit"])
#
# plt.title("Profit Outliers")
#
# plt.show()
#
#
# # Discount
# plt.figure(figsize=(6,4))
#
# plt.boxplot(df["Discount"])
#
# plt.title("Discount Outliers")
#
# plt.show()
#
# # Scatter plot
#
# # Sales v/s Profit
# plt.figure(figsize=(7,5))
#
# plt.scatter(df["Sales"], df["Profit"])
#
# plt.xlabel("Sales")
# plt.ylabel("Profit")
#
# plt.title("Sales vs Profit")
#
# plt.show()

print("==========Phase 4===================")

# Phase 4

# Business KPI Analysis

# Calculate and analyze:
# • Total Revenue
print("-----------Total Revenue--------------------")
total_revenue = df["Sales"].sum()

print(total_revenue)
print("-------Average order value---------------")
# • Average Order Value

order_value = (
    df.groupby("Order ID")["Sales"]
      .sum()
)

average_order_value = order_value.mean()

print(average_order_value)


# • Total Customers
print("--------Total customers-------------------")
total_customers = df["Customer ID"].nunique()

print(total_customers)

# • Repeat Customer Rate
print("---------Repeat customer rate------------------------")
orders_per_customer = (
    df.groupby("Customer ID")["Order ID"]
      .nunique()
)

repeat_customers = (orders_per_customer > 1).sum()

repeat_rate = (
    repeat_customers
    / total_customers
) * 100

print(repeat_rate)

# • Top Categories

print("----------------Top categories--------------")
top_categories = (
    df.groupby("Category")["Sales"]
      .sum()
      .sort_values(ascending=False)
)

print(top_categories)


# • Top Products

print("-----------------------Top 10 products-------------------------")
top_products = (
    df.groupby("Product Name")["Sales"]
      .sum()
      .sort_values(ascending=False)
      .head(10)
)

print(top_products)


# • Monthly Growth

print("--------------------Monthly Growth------------------------------")
monthly = (
    df.groupby(["Order Year",'Order Month'])["Sales"]
      .sum()
      .reset_index()
)

monthly["Growth %"] = (
    monthly["Sales"].pct_change() * 100
)

print(monthly)


# • Average Delivery Time

print("------------------Average delivery time-------------------------")
average_delivery = df["Delivery Time"].mean()

print(average_delivery)


#=================================================================

print("======================================================")
print("Phase 5-Customer segmentation")
print("=========================================")

customer_summary = (
    df.groupby(["Customer ID", "Customer Name"])
      .agg(
          Total_Spending=("Sales", "sum"),
          Number_of_Orders=("Order ID", "nunique")
      )
      .reset_index()
)

customer_summary["Average_Order_Value"] = (
    customer_summary["Total_Spending"] /
    customer_summary["Number_of_Orders"]
)

print(customer_summary.head())
print("------------------------------------------")

q1 = customer_summary["Total_Spending"].quantile(0.25)
q2 = customer_summary["Total_Spending"].quantile(0.50)
q3 = customer_summary["Total_Spending"].quantile(0.75)


def segment_customer(spending):

    if spending >= q3:
        return "Platinum"

    elif spending >= q2:
        return "Gold"

    elif spending >= q1:
        return "Silver"

    else:
        return "Bronze"



customer_summary["Customer Segment"] = (
    customer_summary["Total_Spending"]
    .apply(segment_customer)
)

print(customer_summary.head())
print("-------Count of segment---------------")


segment_counts = (
    customer_summary["Customer Segment"]
    .value_counts()
)

print(segment_counts)
#
# print("Visualization of segment")
#
# plt.figure(figsize=(7,5))
#
# segment_counts.plot(kind="bar")
#
# plt.title("Customer Segment Distribution")
# plt.xlabel("Customer Segment")
# plt.ylabel("Number of Customers")
#
# plt.show()


# File saved for customer segment
# customer_summary.to_csv(
#     "Customer_Segments.csv",
#     index=False
# )

print("===========================================")

#=================================================================================
# Machine learning -prediction of sales
print("Phase -6 Machine learning")
# Use:
# • Linear Regression
# Predict:
# • Future sales based on historical trends

print("Customer segmentation")

customer_df = df.groupby("Customer ID").agg({

    "Sales":"sum",

    "Order ID":"nunique",

    "Quantity":"sum",

    "Discount":"mean",

    "Profit":"sum"

}).reset_index()

# Rename columns
customer_df.columns = [

    "Customer ID",

    "Total Spending",

    "Number of Orders",

    "Total Quantity",

    "Average Discount",

    "Total Profit"

]

# Average order value
customer_df["Average Order Value"] = (

    customer_df["Total Spending"]

    / customer_df["Number of Orders"]

)

# Purchase frequency
customer_df["Purchase Frequency"] = (

    customer_df["Number of Orders"]

)

print(customer_df)
print("==============================")


# Standardize
from sklearn.preprocessing import StandardScaler

features = customer_df[[
    "Total Spending",
    "Number of Orders",
    "Average Order Value",
    "Total Quantity",
    "Average Discount",
    "Total Profit"
]]

scaler = StandardScaler()

scaled = scaler.fit_transform(features)


# Find best K

from sklearn.cluster import KMeans

wcss = []

for i in range(2,11):

    model = KMeans(
        n_clusters=i,
        random_state=42,
        n_init=10
    )

    model.fit(scaled)

    wcss.append(model.inertia_)


# Plotting
plt.figure(figsize=(8,5))

plt.plot(range(2,11),wcss,marker='o')

plt.xlabel("Clusters")

plt.ylabel("WCSS")

plt.title("Elbow Method")

plt.show()


# Silhoutte score
from sklearn.metrics import silhouette_score

for k in range(2,11):

    model = KMeans(
        n_clusters=k,
        random_state=42,
        n_init=10
    )

    labels = model.fit_predict(scaled)

    score = silhouette_score(scaled,labels)

    print(k,score)

# Train
kmeans = KMeans(

    n_clusters=4,

    random_state=42,

    n_init=10

)

# Cluster summary
customer_df["Cluster"] = kmeans.fit_predict(scaled)

cluster_summary = customer_df.groupby("Cluster").mean(numeric_only=True)


cluster_summary.sort_values("Total Spending")



cluster_names = {

    1: "Bronze",
    2: "Silver",
    0: "Gold",
    3: "Platinum"

}
print(cluster_summary)


customer_df["Customer Segment"] = customer_df["Cluster"].map(cluster_names)

print("======================")
print(customer_df)

# Plotting
plt.figure(figsize=(10,6))

plt.scatter(
    customer_df["Total Spending"],
    customer_df["Average Order Value"],
    c=customer_df["Cluster"],
    cmap="viridis",
    s=60
)

plt.xlabel("Total Spending")
plt.ylabel("Average Order Value")
plt.title("Customer Segments using K-Means")

plt.colorbar(label="Cluster")
plt.show()

print("=================")
print("Count of customers in each segment")
print(customer_df["Customer Segment"].value_counts())

# customer_df.to_csv("Customer_Segmentation.csv", index=False)







# Business insights
# Platinum customers contribute the largest share of revenue despite representing a smaller proportion of the customer base.
# Bronze customers make infrequent purchases and have the lowest average spending, making them suitable for re-engagement campaigns.
# Gold customers demonstrate strong loyalty and are good candidates for upselling.
# Regions with a higher concentration of Platinum customers should receive priority for premium marketing initiatives.
# Increasing the Average Order Value of Silver customers could significantly improve overall revenue.


