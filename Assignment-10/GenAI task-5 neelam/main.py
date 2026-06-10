import pandas as pd

students = {
    'Name': ['Amit', 'Neha', 'Rahul', 'Sneha', 'Pooja'],
    'Marks': [78, 85, 90, 66, 72],
    'Subject': ['Math', 'Math', 'Science', 'Science', 'Math']
}

df = pd.DataFrame(students)

print("info():", df.info())
print("describe():", df.describe())
print("head():", df.head())
print("tail():", df.tail())

sorted_df = df.sort_values(by='Marks', ascending=False)
print("sorted by marks:", sorted_df)

sorted_df = sorted_df.reset_index(drop=True)
print("after reset index:", sorted_df)