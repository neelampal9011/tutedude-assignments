import pandas as pd

marks = [78, 85, 90, 66, 72]
series = pd.Series(marks)

print("add 5 :", series + 5)
print("subtract 2 :", series - 2)
print("multiply 1.05:", series * 1.05)
print("divide 2:", series / 2)