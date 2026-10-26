import pandas as pd
df = pd.read_csv('GooglePlayStore_wild.csv')
# Print information about the entire DataFrame to see which columns need to be cleaned
print(df.info())

# How many apps in the dataset have no ('NaN') rating ('Rating')?
print(len(df[pd.isnull(df['Rating'])]))
# Replace the null value ('NaN') of the rating ('Rating') for such apps with -1.
df['Rating'].fillna(-1, inplace = True)

# Determine what other size value ('Size') is stored in the dataset besides Kilobytes and Megabytes, and replace it with -1.
# Convert the app sizes ('Size') to number format (float). The sizes of all the apps must be measured in Megabytes.
print(df['Size'].value_counts())

def set_size(size):
   if size[-1] == 'M':
      return float(size[:-1])
   elif size[-1] == 'k':
      return float(size[:-1]) / 1024
   return -1
df['Size'] = df['Size'].apply(set_size)

# What is the maximum 'Size' of apps in the 'TOOLS' 'Category'?print(df[df['Category'] == 'TOOLS']['Size'].max())
