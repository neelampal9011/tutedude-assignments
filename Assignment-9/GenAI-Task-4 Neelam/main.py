import numpy as np

data = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])
row_sum = np.sum(data, axis=1)
col_sum = np.sum(data, axis=0)
min_val = np.min(data)
max_val = np.max(data)
mean_val = np.mean(data)

print("row sum:", row_sum)
print("column sum:", col_sum)
print("minimum:", min_val)
print("maximum:", max_val)
print("mean:", mean_val)