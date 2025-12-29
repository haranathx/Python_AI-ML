import pandas as pd

data = [100, 102, 104]

# series = pd.Series(data)

# print(series)

series= pd.Series(data, index=["a", "b", "c"])

# .iloc integer location
# .loc location by label

# print(series.loc["c"])
print(series.iloc[0])