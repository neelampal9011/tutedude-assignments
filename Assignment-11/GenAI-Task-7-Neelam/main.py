import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("book_sales.csv")

market_share = df['bookFormat'].value_counts()

plt.figure(figsize=(8,8))

plt.pie(market_share,labels=market_share.index,autopct='%1.1f%%')

plt.title("Market Share by Book Format")

plt.show()