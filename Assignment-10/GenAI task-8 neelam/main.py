import pandas as pd

students = {
    'Name': ['Amit', 'Neha', 'Rahul', 'Sneha', 'Pooja'],
    'Marks': [78, 85, 90, 66, 72],
    'Subject': ['Math', 'Math', 'Science', 'Science', 'Math']
}

df = pd.DataFrame(students)

df.plot(x='Name', y='Marks', kind='bar',title='Student Names vs Marks')

df['Marks'].plot(kind='line',title='Line Graph of Marks')
df['Marks'].plot(kind='hist',title='Histogram of Marks')