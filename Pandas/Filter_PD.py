# Filtering = Keeping the rows that match a condition

import pandas as pd

df = pd.read_csv("Pandas/data.csv")
tall_pokemon =  df[df["Height"]>=2]
heavy_pokemon =  df[df["Weight"]>=150]

print(heavy_pokemon)