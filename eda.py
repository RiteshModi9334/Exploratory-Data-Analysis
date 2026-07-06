import pandas as pd


# Load Dataset
df = pd.read_csv("iris.csv.xls")

print("First 5 Rows:")
print(df.head())
print(df.columns)

print("\nDataset Info:")
print(df.info())

print("\nSummary:")
print(df.describe())

print("\nMissing Values:")
print(df.isnull().sum())

print("\nSpecies Count:")
print(df['variety'].value_counts())


