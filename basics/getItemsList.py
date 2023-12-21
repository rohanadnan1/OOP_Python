from typing import List, Dict, Union

class Product:
    discount = 0.6
    allItems: List[Dict[str, Union[str, int]]] = []
    def __init__(self, name: str, price: int, quantity = 0):
        self.name = name
        self.price = price
        self.quantity = quantity
        assert self.quantity > 0, "Quantity can't be zero or negative."
        assert self.price > 0, "Price can't be zero or negative."
        self.allItems.append({"name": self.name, "price": self.price, "quantity": self.quantity})

    def getPrice(self):
        return f'Price of {self.quantity} {self.name} is {self.price * self.quantity} PKR.'
    
    def getDiscountPrice(self):
        return f'Discounted Price of {self.quantity} {self.name} is {round(self.price * self.quantity * self.discount)} PKR.'

    def __repr__(self) -> str:
        return f'{self.name}'

iphone = Product("iPhone 12", 200000, 10)
android = Product("Samsung Galaxy S21", 150000, 10)
lg = Product("LG Wing", 100000, 10)

for product in Product.allItems:
    print(product)
    if product['name'].lower() == 'iphone 12':
        print(f'Yes we have iPhone 12 in our inventory. And its price is {product["price"]}.')
        break
    else:
        print(f'Sorry we dont have iPhone 12 in our inventory.')
        break


