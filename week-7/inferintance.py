
class Product:
    def __init__(self, price):
        self.price = price

    def get_price(self):
        return self.price

class DiscountedProduct(Product):
    def get_price(self):
        price = super().get_price()  # super(). powoduje że odwołujemy się do get_price z class Product
        return price - 0.1 * price

product = DiscountedProduct(100)
print(product.get_price())



