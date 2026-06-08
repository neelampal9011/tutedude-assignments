import numpy as np

marks = np.array([78, 85, 90, 66, 72, 88, 95, 60])

mean = np.mean(marks)
median = np.median(marks)
variance = np.var(marks)
std_dev = np.std(marks)
min_val = np.min(marks)
max_val = np.max(marks)
range_val = max_val - min_val

print("mean:", mean)
print("median:", median)
print("variance:", variance)
print("standard deviation:", std_dev)
print("minimum:", min_val)
print("maximum:", max_val)
print("range:", range_val)
