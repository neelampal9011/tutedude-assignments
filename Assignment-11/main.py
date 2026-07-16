import matplotlib.pyplot as plt
import pandas as pd
 
sales = pd.read_csv("book_sales.csv")
print(sales)

print(sales.head(10))
print(sales.columns)