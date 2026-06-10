import pandas as pd

students = {
    'Name': ['Amit', 'Neha', 'Rahul', 'Sneha', 'Pooja'],
    'Marks': [78, 85, 90, 66, 72],
    'Subject': ['Math', 'Math', 'Science', 'Science', 'Math']
}

df = pd.DataFrame(students)

print("first 3 rows:", df.head(3))
print("last 2 rows:", df.tail(2))
print("shape:", df.shape)
print("column names:", df.columns)