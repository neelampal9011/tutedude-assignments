from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

class CreditCardPayment(Payment):
    def process_payment(self, amount):
        print(f"processing Credit Card payment of rupees: {amount}")

class UPIPayment(Payment):
    def process_payment(self, amount):
        print(f"processing UPI payment of rupees: {amount}")
        
cc_pay = CreditCardPayment()
upi_pay = UPIPayment()

cc_pay.process_payment(150.50)
upi_pay.process_payment(45)
