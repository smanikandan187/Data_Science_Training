import numpy as np

data = np.array([
    [25, 50000, 3],
    [30, 60000, 5],
    [22, 45000, 2],
    [35, 80000, 7],
    [28, 52000, 4],
    [40, 90000, 10]
])

print("Shape of Data:", data.shape)
print("Total Rows:", data.shape[0])
print("Total Columns:", data.shape[1])

print("\nMean:", np.mean(data, axis=0))
print("Median:", np.median(data, axis=0))
print("Standard Deviation:", np.std(data, axis=0))
print("Minimum:", np.min(data, axis=0))
print("Maximum:", np.max(data, axis=0))

print("\nAre there any NaNs? ->", np.isnan(data).any())

print("\n25th Percentile:", np.percentile(data, 25, axis=0))
print("75th Percentile:", np.percentile(data, 75, axis=0))
