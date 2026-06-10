import pandas as pd

marks = [78, 85, 90, 66, 72]
series = pd.Series(marks)

print("Series Values:", series)
print("Index:", series.index)
print("Data Type:", series.dtype)
print("First Element:", series[0])
print("Last Two Elements:", series[-2:])
