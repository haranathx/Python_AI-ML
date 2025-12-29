import pandas as pd


data={
    "Name": ["Spongebob", "Patric", "Squidward"],
    "Age": [30,35,50]
}

# datafame==df

# when we use only the data index will start from 0 
# But we can customize the index like below

df= pd.DataFrame(data,index=["Emp 1","Emp 2","Emp 3"])

# print all data
# print(df)

# print specific data using label location

# print(df.loc["Emp 1"])

# add a new column
df["Job"]=["Cook", "N/A", "Cashier"]


# add a new rows
new_rows = pd.DataFrame([{"Name": "Sandy", "Age": 28, "Job": "Engineer"},
                         {"Name": "gauss", "Age": 58, "Job": "Manager"}],
                         index=["Emp 4", "Emp 5"])

df=pd.concat([df, new_rows])
print(df)