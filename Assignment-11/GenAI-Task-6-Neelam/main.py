import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("book_sales.csv")

plt.figure(figsize=(8,5))

plt.hist(df['price'], bins=20)

plt.title("Distribution of Book Prices")
plt.xlabel("Price")
plt.ylabel("Frequency")

plt.show()