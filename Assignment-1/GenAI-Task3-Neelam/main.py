# 1.creat dictionary
price_dict = {
    "laptop":1800,
    "phone":800,
    "tablet":500,
    "headphones":150,
    "mouse":40,
    "keyboard":70
}
print(price_dict)

# 2. add a new product
price_dict["monitor"] = 300

price_dict["phone"] = 850      # update the price of existing product

product_to_remove = 'tablet'   # remove a product safely

if product_to_remove in price_dict:
    del price_dict[product_to_remove]
else:
    print(product_to_remove,"not found")

print(f"updated price dictionary :", price_dict)


# 3
average_price = sum(price_dict.values()) / len(price_dict)
print('average price :',average_price)

# extra questions
max_value = max(price_dict.values())
print(max_value)
min_value = min(price_dict.values())
print(min_value)
