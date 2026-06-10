import pandas as pd

sales = {
    'Day': ['Mon', 'Tue', 'Wed', 'Thu', 'Fri'],
    'Revenue': [1200, 1500, 900, 2000, 1800]
}

df = pd.DataFrame(sales)

total_revenue = df['Revenue'].sum()
print("total revenue:", total_revenue)
avg_revenue = df['Revenue'].mean()
print("average daily revenue:", avg_revenue)
highest_day = df.loc[df['Revenue'].idxmax()]
print("day with highest revenue:", highest_day)
print("days where Revenue > Average:", df[df['Revenue'] > avg_revenue])
df.plot(x='Day', y='Revenue', kind='line', title='Revenue vs Day')