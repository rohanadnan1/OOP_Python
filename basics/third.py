class Product:
    def __init__(self, name, price, quantity=0):
        self.name = name
        self.price = price
        self.quantity = quantity

    def getPrice(self):
        if self.quantity == 0 or self.quantity < 0:
            print('-------------------------------------------')
            return f'{self.name} is out of stock.'
        
        print('-------------------------------------------')
        totalPrice = int(self.price) * int(self.quantity)
        return f'Price of {self.quantity} {self.name} is {totalPrice} PKR.'



iphone = Product("iPhone 12", 200000, 10)   
print(iphone.getPrice())     

android = Product("Samsung Galaxy S21", 150000, 0)
print(android.getPrice())