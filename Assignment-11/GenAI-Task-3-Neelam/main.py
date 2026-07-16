import matplotlib.pyplot as plt
import pandas as pd

sales = pd.read_csv("book_sales.csv")
sales['bookPublishedDate'] = pd.to_datetime(sales['bookPublishedDate'])
sales['bookPublishedDate'] = sales['bookPublishedDate'].dt.month_name()

monthly_sales = sales.groupby('bookPublishedDate')['price'].sum()
x = monthly_sales.index
y = monthly_sales.values

plt.figure(figsize=(12,6))
plt.title('Monthly Sales',color='red')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.bar(x,y,color='green')
plt.show()


x = monthly_sales.values
y = monthly_sales.index

plt.figure(figsize=(12,8))
plt.title('Monthly Sales',color='blue')
plt.xlabel('Sales')
plt.ylabel('Month')
plt.barh(y,x,color='green')
plt.show()
