f = open("products.txt", "w")

for i in range(3):
    product_name = input("Enter product name: ")
    price = input("Enter product price: ")

    f.write(product_name + " | " + price + "\n")

f.close()

print("product List:")
f = open("products.txt", "r")
print(f.read())
f.close()