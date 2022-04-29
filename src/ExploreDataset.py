import pandas as pd

# Read csv file
df = pd.read_csv("/Users/Dani/workspace/EikaCase/resources/loan.csv")

print('Printing default loan dataframe:')
print(df.info())

is_id_unique = df['id'].is_unique
print('Is id column values unique:', is_id_unique)

is_member_id_unique = df['member_id'].is_unique
print('Is member id column values unique:', is_member_id_unique)