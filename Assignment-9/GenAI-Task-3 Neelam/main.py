import numpy as np

values = np.array([2, 4, 6, 8, 10])

sqrt_vals = np.sqrt(values)
exp_vals = np.exp(values)
log_vals = np.log(values)
total_sum = np.sum(values)
cumsum_vals = np.cumsum(values)

print("original array:", values)
print("square root:", sqrt_vals)
print("exponential:", exp_vals)
print("log:", log_vals)
print("sum:", total_sum)
print("cumulative sum:", cumsum_vals)