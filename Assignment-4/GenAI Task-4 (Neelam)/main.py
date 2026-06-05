with open('sales_data.txt', "r") as f:
    content = f.read()
    print(content)

with open('sales_data.txt', "r") as f:
    sales = f.readlines()
    sales = [int(line.strip()) for line in sales]
    print(sales)

total_sales = sum(sales)
print("Total Sales:", total_sales)

highest_sale = max(sales)
print("Highest Sale:", highest_sale)

lowest_sale = min(sales)
print("Lowest Sale:", lowest_sale)

average_sale = total_sales / len(sales)
print("Average Sale:", average_sale)