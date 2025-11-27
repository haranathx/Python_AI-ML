# Making folders in bulk

import os

if (not os.path.exists("Data")):
    os.mkdir("OS module/Data")

for i in range (0, 100):
    os.mkdir(f"OS module/Data/Day{i+1}")