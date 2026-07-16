import matplotlib.pyplot as plt
import pandas as pd

sales = pd.read_csv('book_sales.csv')
print(sales)
print(sales.info())

sales['bookPublishedDate'] = pd.to_datetime(sales['bookPublishedDate'])
sales['bookPublishedDate'] = sales['bookPublishedDate'].dt.year

yearly_sales = sales.groupby('bookPublishedDate')['price'].sum()
x = yearly_sales.index
y = yearly_sales.values

plt.figure(figsize = (10,5))
plt.title('Yearly Sales',color='purple')
plt.xlabel('Year')
plt.ylabel('Sales')
plt.scatter(x,y,color='red')
plt.show()
