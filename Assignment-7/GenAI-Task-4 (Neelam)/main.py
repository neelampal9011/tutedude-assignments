class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Laptop(Product):
    def __init__(self, name, price, storage):
        super().__init__(name, price)
        self.storage = storage

    def get_info(self):
        return f"Laptop: {self.name} , Price: {self.price} , Specs: {self.storage}"

class Mobile(Product):
    def __init__(self, name, price, network):
        super().__init__(name, price)
        self.network = network

    def get_info(self):
        return f"Mobile: {self.name} , Price: {self.price} , Connectivity: {self.network}"

devices = [
    Laptop("asus", 99999, "512GB"),
    Mobile("one plus", 79999, "5G"),
    Laptop("MacBook Air", 129999, "512GB")
]

for device in devices:
    print(device.get_info())

