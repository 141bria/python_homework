import pandas as pd

# Sample DataFrames

df1 = pd.DataFrame({
    'ID': [1, 2, 3],
    'Date': ['2021-01-01', '2021-01-02', '2021-01-03'],
    'Name': ['Alice', 'Bob', 'Charlie']
})
print(df1)
df2 = pd.DataFrame({
    'ID': [1, 2, 3],
    'Date': ['2021-01-01', '2021-01-02', '2021-01-03'],
    'Score': [85, 92, 88]
})
print(df2)
# Merge on both 'ID' and 'Date'
merged_df = pd.merge(df1, df2, on=['ID', 'Date'], how='inner')
print(merged_df)