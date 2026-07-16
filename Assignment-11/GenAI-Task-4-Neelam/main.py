import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("book_sales.csv")

books = df['title'].head(10)
current_price = df['price'].head(10)
old_price = df['oldPriceFloat'].head(10)

x = range(len(books))
w = 0.4

plt.figure(figsize=(10,5))

plt.bar([i-w/2 for i in x], current_price,
        width=w, label='Current Price')

plt.bar([i+w/2 for i in x], old_price,
        width=w, label='Old Price')

plt.xticks(x, books, rotation=90)


plt.title("Current Price vs Old Price")
plt.xlabel("Book Title")
plt.ylabel("Price")
plt.legend()

plt.show()