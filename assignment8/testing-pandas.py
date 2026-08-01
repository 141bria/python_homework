import pandas as pd
#
data = {
    'Name':['Amara','Yula','Carlos'],
    'Age':[24,27,22],
    'City': ['New York','San Francisco','Chicago']
}
df=pd.DataFrame(data)
print(df)
import pandas as pd

# Sample DataFrame with missing values
data = {'Name': ['Amara', 'Yulia', None, 'David'],
        'Age': [24, 27, 22, None],
        'Score': [85, None, 88, 76]}
df = pd.DataFrame(data)

# Find rows with missing data
df_missing = df[df.isnull().any(axis=1)]
print(df_missing)
# Remove rows with missing data
df_dropped = df.dropna()
print(df_dropped)

# Replace missing data with default values
df_filled = df.fillna({'Age': 0, 'Score': df['Score'].mean()})
print(df_filled)