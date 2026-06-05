class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_info(self):
        return f"Product: {self.name}, Price: ${self.price:.2f}"

class ElectronicProduct(Product):
    def __init__(self, name, price, warranty_years):
        super().__init__(name, price)
        self.warranty_years = warranty_years

    def get_info(self):
        base_info = super().get_info()
        return f"{base_info}, warranty: {self.warranty_years} years"

laptop = ElectronicProduct("laptop", 50000, 2)
print(laptop.get_info())
