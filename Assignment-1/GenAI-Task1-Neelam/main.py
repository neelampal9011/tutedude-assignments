# 1. create a list of product names
product = ["laptop", "phone", "tablet", "headphone", "keyboard", "mouse"]

# 2. create a tuple of a sample product
sample_product = ("laptop", 1800, "electronics")

# 3. print the second and last product in the list
print("The second product is:", product[1])
print("The last product is:", product[-1])

# 4. add two new products to the list
product.append("monitor")
product.append("speaker")
print("The updated list is:", product)

#extra(optional) questions
sample_product_list = list(sample_product)
sample_product_list[1] = 2000
sample_product = tuple(sample_product_list)
print("The updated tuple is:", sample_product)