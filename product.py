
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = max(0, price)
        self.quantity = max(0, quantity)

    
    def calculateTotal(self):
        return self.price * self.quantity
