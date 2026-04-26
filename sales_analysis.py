import pandas as pd

# Load dataset
df = pd.read_csv("sales_data.csv")

print("Dataset Preview:")
print(df.head())

# Handle missing values
df.fillna(0, inplace=True)

# Convert Total_Sales column
df['Total_Sales'] = pd.to_numeric(df['Total_Sales'], errors='coerce')

# Remove invalid rows
df.dropna(inplace=True)

# 🔹 Metric 1: Total Sales
total_sales = df['Total_Sales'].sum()

# 🔹 Metric 2: Best-Selling Product
best_product = df.groupby('Product')['Total_Sales'].sum().idxmax()

# 🔹 Metric 3: Average Sales
average_sales = df['Total_Sales'].mean()

# 🔹 Metric 4: Total Quantity Sold
total_quantity = df['Quantity'].sum()

# 🔹 Metric 5: Top 3 Products
top_products = df.groupby('Product')['Total_Sales'].sum().sort_values(ascending=False).head(3)

# Output
print("\n--- Sales Analysis Report ---")
print(f"Total Sales: {total_sales}")
print(f"Best Selling Product: {best_product}")
print(f"Average Sales: {average_sales}")
print(f"Total Quantity Sold: {total_quantity}")
print("\nTop 3 Products:")
print(top_products)
