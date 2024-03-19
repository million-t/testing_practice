from shopcart import Product, ShoppingCart


class Test:
    def __init__(self):
        self.unitTest()
        self.intergrationTestPositive()
        self.intergrationTestZero()
        self.intergrationTestNegative()
        self.integratioinTestEmpty()
        print('=================')
        print('All tests passed!')
        print('=================')

    def unitTest(self):
        product = Product('phone', 1000, 11)
        assert product.name == 'phone', "name failed"
        assert product.price == 1000, "price failed"
        assert product.quantity == 11, "quantity failed"
        assert product.calculateTotal() == 11000, "calculateTotal failed"
        print('Unit test passed.')


    def integratioinTestEmpty(self):
        cart = ShoppingCart()
        assert cart.calculateTotal() == 0, "calculateTotal failed on Empty"
        print('Integration test with empty cart passed.')

    def intergrationTestPositive(self):
        product1 = Product('phone', 1000, 11)
        product2 = Product('laptop', 2000, 5)
        cart = ShoppingCart()
        cart.addProduct(product1)
        cart.addProduct(product2)
        assert cart.cart == [product1, product2], 'cart failed'
        assert cart.calculateTotal() == 21000, "calculateTotal failed on positive"
        print('Integration test with positive quantity passed.')

    def intergrationTestZero(self):
        product1 = Product('phone', 1000, 0)
        cart = ShoppingCart()
        cart.addProduct(product1)
        assert cart.calculateTotal() == 0, "calculateTotal failed on zero"
        print('Integration test with zero quantity passed.')
    
    def intergrationTestNegative(self):
        product1 = Product('phone', 1000, -1)
        cart = ShoppingCart()
        cart.addProduct(product1)
        assert cart.calculateTotal() == 0, "calculateTotal failed on negative"
        print('Integration test with negative quantity passed.')
        


Test()