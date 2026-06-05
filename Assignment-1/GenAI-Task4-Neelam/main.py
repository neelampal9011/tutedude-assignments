product = ["laptop", "phone", "tablet", "headphone", "keyboard", "mouse"]
categories = ["electronics", "electronics", "electronics", "accessories", "accessories", "accessories"]
price_dict = {
    "laptop":1800,
    "phone":800,
    "tablet":500,
    "headphone":150,
    "mouse":40,
    "keyboard":70
}

# 1. create catalog list of tuples

catalog=[]

for i in range(len(product)):
    product_name = product[i]
    price = price_dict[product_name]
    category = categories[i]

    catalog.append((product_name, price, category))

print("catalog: ", catalog)

# 2. create category_to_products dictionary

category_to_products = {}

for product_name, price, category in catalog:
    if category not in category_to_products:
        category_to_products[category]=[]

    category_to_products[category].append(product_name)

print("category to products:", category_to_products)

# 3. print product frome category with max product
max_category = max(category_to_products, key= lambda x: len(category_to_products[x]))
print("category with maximum products:",max_category)
print("product in this category:", category_to_products[max_category])

