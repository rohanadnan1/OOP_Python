class Animal:
    nature = 'animal'
    def __init__(self, name):
        self.name = name
        
        

class Cow(Animal):
    def __init__(self, name):
        super().__init__(name)

    def __str__(self):
        return f'Hello, my name is {self.name} and I am a cow. And my nature is {self.nature}'   

mycow = Cow('Betsy')
print(mycow)     


class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)

    nature = 'friendly'
    def __str__(self):
        return f'Hello, my name is {self.name} and I am a cat. And my nature is {self.nature}'
    
mycat = Cat('Garfield')
print(mycat)

# to check where these child classes are coming from
print(Cow.__bases__, Cat.__bases__)