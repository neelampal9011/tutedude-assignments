import pandas as pd

marks = pd.Series([78, 85, 90, 66, 72])

print("maximum marks:", marks.max())
print("minimum marks:", marks.min())
print("sum of marks:", marks.sum())
print("mean marks:", marks.mean())
passed = marks.apply(lambda x: x >= 70)

print("pass status:", passed)
print("number of students passed:", passed.sum())