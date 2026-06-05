class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def __str__(self):
        return f"name: {self.name},price: {self.price},category: {self.category}"

    def __add__(self, other):
        if isinstance(other, Product):
            return self.price + other.price
        return "error"

product1 = Product("mouse", 25.50, "electronics")
product2 = Product("keyboard", 85.00, "electronics")

print(product1)
print(product2)

total_combined_price = product1 + product2
print("total combined price: " + str(total_combined_price))
