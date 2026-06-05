class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def get_info(self):
        print("Name:", self.name)
        print("Price:", self.price)
        print("Category:", self.category)

    def apply_discount(self, percent):
        discount = (self.price*percent)/100
        return self.price-discount

product1 = Product("laptop", 50000, "electronics")
product2 = Product("phone", 20000, "electronics")

product1.get_info()
product2.get_info()

print("discounted Price:", product1.apply_discount(10))