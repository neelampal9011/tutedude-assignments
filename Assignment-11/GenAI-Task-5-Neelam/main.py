import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("book_sales.csv")

books = df['title'].head(10)
current_price = df['price'].head(10)
old_price = df['oldPriceFloat'].head(10)

plt.figure(figsize=(10,6))

plt.bar(books, current_price, label="Current Price",color='green')

plt.bar(books, old_price,
        bottom=current_price,
        label="Old Price",color='red')

plt.xticks(rotation=90)

plt.title("Stacked Bar Chart")
plt.xlabel("Book Title")
plt.ylabel("Price")
plt.legend()

plt.show()