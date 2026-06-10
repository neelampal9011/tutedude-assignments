import pandas as pd

students = {
    'Name': ['Amit', 'Neha', 'Rahul', 'Sneha', 'Pooja'],
    'Marks': [78, 85, 90, 66, 72],
    'Subject': ['Math', 'Math', 'Science', 'Science', 'Math']
}

df = pd.DataFrame(students)

print("students scoring more than 75:", df[df['Marks'] > 75])
print("math students:", df[df['Subject'] == 'Math'])
average_marks = df['Marks'].mean()

print("students scoring above average:", df[df['Marks'] > average_marks])
print("failed students:", df[df['Marks'] < 70])