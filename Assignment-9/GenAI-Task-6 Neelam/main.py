import numpy as np

marks = np.array([78, 85, 90, 66, 72, 88, 95, 60])

sorted_marks = np.sort(marks)

p25 = np.percentile(marks, 25)
p50 = np.percentile(marks, 50)
p75 = np.percentile(marks, 75)
mean_val = np.mean(marks)
above_avg = marks[marks > mean_val]

print("sorted marks :", sorted_marks)
print("25th percentile :", p25)
print("50th percentile :", p50)
print("75th percentile :", p75)
print("above average count :", len(above_avg))