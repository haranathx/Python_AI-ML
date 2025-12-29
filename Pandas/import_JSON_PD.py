import pandas as pd

df= pd.read_json("Pandas/data.json")

# print truncate version
print(df)

# # to print entire dataframe
print(df.to_string())