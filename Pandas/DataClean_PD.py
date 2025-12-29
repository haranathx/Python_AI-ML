# Data cleaning = the process of fixing or removing:
#                 incomplete, incorrect, or irrelevant data.
import pandas as pd

df = pd.read_csv("Pandas/data.csv")

# 1. Drop irrelevant columns
# df = df.drop(columns=["Legendary"])

# 2. Handle missing data
# df= df.dropna(subset=["Type2"])
# df= df.fillna({"Type2": "None"})

# 3. Fix inconsistent values 

# df["Type1"] = df["Type1"].replace({"Grass": "GRASS",
#                                    "Fire":"FIRE",
#                                    "Water":"WATER"})

# print(df.to_string())

# 4. Standardized text

# df["Name"] = df["Name"].str.lower()

# 5. Fix data types
# df["Legendary"] = df["Legendary"].astype(bool)

# 6. Remove duplicates
df= df.drop_duplicates()

print(df.to_string())

