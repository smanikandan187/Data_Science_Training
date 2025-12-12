import pandas as pd

df = pd.DataFrame({
    'Age': [25, 30, 22, 35, 28, 40],
    'Salary': [50000, 60000, 45000, 80000, 52000, 90000],
    'Experience': [3, 5, 2, 7, 4, 10]
})

print("First 5 rows:\n", df.head())
print("\nShape:", df.shape)
print("\nData Types:\n", df.dtypes)

print("\nSummary Statistics:\n", df.describe())

print("\nMissing Values:\n", df.isnull().sum())

