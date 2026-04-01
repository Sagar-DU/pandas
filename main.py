import pandas as pd

# Create a DataFrame from a dictionary
df = pd.DataFrame({
    "name": ["Alice", "Bob", "Charlie"],
    "age": [25, 30, 35],
    "city": ["New York", "Los Angeles", "Chicago"],
    "salary": [70000, 80000, 90000]
})

# Display the DataFrame
print("DataFrame:")
print(df)

# Display the first 2 rows of the DataFrame
print("\nFirst 2 rows of the DataFrame:")
print(df.head(2))

# Display the structure of the DataFrame
print("\nStructure of the DataFrame:")
print(df.info())

# Display summary statistics of the DataFrame
print("\nSummary statistics of the DataFrame:")
print(df.describe())
