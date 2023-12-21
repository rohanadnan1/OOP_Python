class Mobile:
    def __init__(self, name: str, price: int, quantity = 0):
        self.name = name
        self.price = price
        self.quantity = quantity

    def getPrice(self):
        assert self.quantity > 0, "Quantity can't be zero or negative."
        assert self.price > 0, "Price can't be zero or negative."
        return f'Price of {self.quantity} {self.name} is {self.price * self.quantity} PKR.'    

iphone = Mobile("iPhone 12", 200000, 10)
print(iphone.getPrice())

newAndroid = Mobile("Samsung Galaxy S21", 150000, 0)
print(newAndroid.getPrice())