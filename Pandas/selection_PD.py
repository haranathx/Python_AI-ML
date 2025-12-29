import pandas as pd

df= pd.read_csv("Pandas/data.csv")

# Selection by Column
# ---------------------

# truncate version
# print(df["Name"])

# full version
# print(df["Name"].to_string())
# print(df["Height"].to_string())

# and so on...

# Select multiple column

# print(df[["Name","Height","Weight"]])

# print(df[["Name","Height","Weight"]].to_string())
# ===================================================================================

# Selection by Row/S
# print(df.loc[0])


df= pd.read_csv("Pandas/data.csv", index_col="Name")
print(df.loc["Pikachu"])