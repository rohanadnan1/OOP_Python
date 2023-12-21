class Product:
    discout = 0.8
    def __init__(self,name:str,price: int,quantity = 0):
        self.name = name
        self.price = price
        self.quantity = quantity
        assert self.quantity > 0, "Quantity can't be zero or negative."
        assert self.price > 0, "Price can't be zero or negative."

    def getPrice(self):
        return f'Price of {self.quantity} {self.name} is {self.price * self.quantity} PKR.'
    
    def getDiscountPrice(self):
        return f'Discounted Price of {self.quantity} {self.name} is {round(self.price * self.quantity * self.discout)} PKR.'
    
iphone = Product("iPhone 12", 200000, 10)
print(iphone.getPrice())
print(iphone.getDiscountPrice())
