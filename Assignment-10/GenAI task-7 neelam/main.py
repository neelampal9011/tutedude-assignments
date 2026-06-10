import pandas as pd

students = {
    'Name': ['Amit', 'Neha', 'Rahul', 'Sneha', 'Pooja'],
    'Marks': [78, 85, 90, 66, 72],
    'Subject': ['Math', 'Math', 'Science', 'Science', 'Math']
}

df = pd.DataFrame(students)

print("average marks per subject:", df.groupby('Subject')['Marks'].mean())
print("number of students per subject:", df.groupby('Subject')['Name'].count())
print("maximum marks per subject:", df.groupby('Subject')['Marks'].max())