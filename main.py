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

# Display the column names of the DataFrame
print("\nColumn names of the DataFrame:")
print(df.columns)

# Display the data types of each column
print("\nData types of each column:")
print(df.dtypes)

# Display the shape of the DataFrame
print("\nShape of the DataFrame:")
print(df.shape)

# Display the index of the DataFrame
print("\nIndex of the DataFrame:")
print(df.index)

# Display the values of the DataFrame
print("\nValues of the DataFrame:")
print(df.values)