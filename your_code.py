import pandas as pd

# Uploading dataframe 
df = pd.read_csv('GoogleApps.csv')


# What is the name of the first application containing in the dataset?
print(df.head())

# What is the category of the last application containing in the dataset?
print(df.tail())

# How many columns are there in the dataset?
# What is the type of data stored in each column?
print(df.info())

# Specify the arithmetic mean and median for the size of the applications.
# How much does the most expensive application cost?
# *Specify the arithmetic mean and median for the number of application installs.
print(df.describe())
