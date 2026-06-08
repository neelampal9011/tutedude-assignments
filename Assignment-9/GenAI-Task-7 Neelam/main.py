import numpy as np

sales = np.array([1200, 1500, 900, 2000, 1800, 1700, 1600])

total_sales = np.sum(sales)

average_sales = np.mean(sales)
highest_day = np.argmax(sales) + 1  
lowest_day = np.argmin(sales) + 1

highest_sales = np.max(sales)
lowest_sales = np.min(sales)

std_dev = np.std(sales)
above_avg_days = np.where(sales > average_sales)[0] + 1

print("total weekly sales : ", total_sales)
print("average daily sales : ", average_sales)
print("highest sales : ", highest_sales, "on day : ", highest_day)
print("lowest sales : ", lowest_sales, "on day : ", lowest_day)
print("standard deviation : ", std_dev)
print("days above average : ", above_avg_days)
