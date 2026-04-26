import pandas as pd

# Load dataset
try:
    df = pd.read_csv("sales_data.csv")
except FileNotFoundError:
    print("File not found. Check file path.")
    exit()

print("Dataset Preview:")
print(df.head())

# Show columns
print("\nColumns:", df.columns)

# Handle missing values
df = df.dropna()

# Convert Sales column safely
if 'Sales' in df.columns:
    df['Sales'] = pd.to_numeric(df['Sales'], errors='coerce')
else:
    print("Sales column not found!")
    exit()

df = df.dropna()

# Check if data exists
if df.empty:
    print("No data available after cleaning!")
    exit()

# Metrics
total_sales = df['Sales'].sum()

best_product = df.groupby('Product')['Sales'].sum().idxmax() if 'Product' in df.columns else "N/A"

average_sales = df['Sales'].mean()

total_quantity = df['Quantity'].sum() if 'Quantity' in df.columns else "N/A"

top_products = df.groupby('Product')['Sales'].sum().sort_values(ascending=False).head(3) if 'Product' in df.columns else "N/A"

# Output
print("\n--- Sales Analysis Report ---")
print(f"Total Sales: {total_sales}")
print(f"Best Selling Product: {best_product}")
print(f"Average Sales: {average_sales}")
print(f"Total Quantity Sold: {total_quantity}")
print("\nTop 3 Products:")
print(top_products)