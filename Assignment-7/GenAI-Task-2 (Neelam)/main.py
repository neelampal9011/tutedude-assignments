class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.category = category
        self.__price = price 

    def get_price(self):
        return self.__price

    def set_price(self, new_price):
        if new_price > 0:
            self.__price = new_price
        else:
            print("Invalid price! Must be greater than 0")

    def get_info(self):
        print("Name:", self.name)
        print("Price:", self.__price)
        print("Category:", self.category)

product1 = Product("laptop", 50000, "electronics")

print("original price:", product1.get_price())

product1.set_price(45000)
print("updated price:", product1.get_price())
product1.set_price(-100)
product1.get_info()