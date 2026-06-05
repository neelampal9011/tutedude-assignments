product = ["laptop", "phone", "tablet", "headphone", "keyboard", "mouse"]
categories = ["electronics", "electronics", "electronics", "accessories", "accessories", "accessories"]

# 1. create a set of categories
categories_set = set(categories)
print("The set of categories is:", categories_set)

# 2. add new categories to the set and show duplicates ignored
categories_set.add("gaming")
categories_set.add("electronics")  #duplicate

print("The updated set of categories is:", categories_set)

# 3. check whether a category exists
category = input("Enter a category: ")
if category in categories_set:
    print(True)
else:
    print(False)
    
# extra(optional)
unique_categories = len(categories_set)
print(f'total unique categories : {unique_categories}')
