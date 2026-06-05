class Product:
    def __init__(self, name, price, category="General"):
        self.name = name
        self.price = price
        self.category = category

    def __str__(self):
        return f"Product(name: '{self.name}', price: {self.price}, category: '{self.category}')"

    def __add__(self, other):
        if isinstance(other, Product):
            return self.price + other.price
        return 'invaild input'  

class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product):
        self.products.remove(product)
                

    def get_total_value(self):
        total = 0
        for product in self.products:
            total += product.price
        return total

    def show_all_products(self):
        if not self.products:
            print("Inventory is currently empty.")
            return
        for product in self.products:
            print(product)

class Store:
    def __init__(self, store_name):
        self.store_name = store_name
        self.inventory = Inventory()

    def add_new_product(self):
        print(self.store_name)
        name = input("Enter product name: ")
        price = float(input("Enter product price: "))
        category = input("Enter product category: ")
        
        new_product = Product(name, price, category)
        self.inventory.add_product(new_product)
        print(f"successfully added: {name}")

    def show_summary(self):
        print(f"store name: {self.store_name}")
        print(f"total items in stock: {len(self.inventory.products)}")
        print(f"total value: {self.inventory.get_total_value()}")
        self.inventory.show_all_products()

my_store = Store("Tech World")

for i in range(3):
    my_store.add_new_product()

my_store.show_summary()

if len(my_store.inventory.products) >= 2:
    prod1 = my_store.inventory.products[0]
    prod2 = my_store.inventory.products[1]
    combined_price = prod1 + prod2
    print(f"total combined cost: {combined_price}")
