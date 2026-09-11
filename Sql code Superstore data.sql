-- 1. Total Orders
SELECT COUNT(DISTINCT "order_id") AS total_orders
FROM Superstore_data;


-- 2. Total Customers
SELECT COUNT(DISTINCT "customer_id") AS total_customers
FROM Superstore_data;


-- 3. Total Products
SELECT COUNT(DISTINCT "product_id") AS total_products
FROM Superstore_data;


-- 4. Monthly Sales
SELECT
    strftime('%Y-%m', "order_date") AS order_month,
    ROUND(SUM("Sales"), 2) AS monthly_sales
FROM Superstore_data
GROUP BY order_month
ORDER BY order_month;


-- 5. Top-Selling Products
SELECT
    "product_id",
    "product_name",
    ROUND(SUM("Sales"), 2) AS total_sales
FROM Superstore_data
GROUP BY "product_id", "product_name"
ORDER BY total_sales DESC
LIMIT 10;


-- 6. Top Customers
SELECT
    "customer_id",
    "customer_name",
    ROUND(SUM("Sales"), 2) AS total_spending
FROM Superstore_data
GROUP BY "customer_id", "customer_name"
ORDER BY total_spending DESC
LIMIT 10;


-- 7. Revenue by Category
SELECT
    "Category",
    ROUND(SUM("Sales"), 2) AS total_revenue
FROM Superstore_data
GROUP BY "Category"
ORDER BY total_revenue DESC;


-- 8. Revenue by State
SELECT
    "State",
    ROUND(SUM("Sales"), 2) AS total_revenue
FROM Superstore_data
GROUP BY "State"
ORDER BY total_revenue DESC;