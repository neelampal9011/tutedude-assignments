import matplotlib.pyplot as plt
import pandas as pd
 
sales = pd.read_csv("book_sales.csv")
print(sales)
print(sales.head())
print(sales.info())

sales['bookPublishedDate'] = pd.to_datetime(sales['bookPublishedDate'])
sales['bookPublishedDate'] = sales['bookPublishedDate'].dt.month_name()

monthly_sales = sales.groupby('bookPublishedDate')['price'].sum()
x = monthly_sales.index
y = monthly_sales.values

plt.figure(figsize = (10,5))
plt.title('monthly sales')
plt.xlabel('month')
plt.ylabel('sales')
plt.plot(x, y, linewidth=1.5, linestyle="--", color='green', marker='d')
plt.grid()
plt.show()