from product import Product


class ShoppingCart:
    def __init__(self):
        self.cart = []
    
    def addProduct(self, product):
        self.cart.append(product)
    
    def calculateTotal(self):
        total = 0
        for product in self.cart:
            total += product.calculateTotal()
        return total

