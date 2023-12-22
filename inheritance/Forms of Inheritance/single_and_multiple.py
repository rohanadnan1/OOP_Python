# Types of inheritance:

'''
Single Inheritance:
This is a form of inheritance in which a class inherits only one parent class. This is the simple form of inheritance and hence, is also referred to as simple inheritance.
'''

class Parent:
    def __init__(self):
        print('Parent class constructor called')

class Child(Parent):
    def __init__(self):
        super().__init__()
        print('Child class constructor called')

# obj0 = Parent()
# obj1 = Child() 

# print(obj0, obj1)



'''
Multiple Inheritance:
An inheritance becomes multiple inheritances when a class inherits more than one parent class. The child class, after inheriting properties from various parent classes, has access to all of its objects.
'''

class Father:
    def __init__(self,name):
        self.fathername = name

    def getFatherName(self):
        return self.fathername    

class Mother:
    def __init__(self,name):
        self.mothername = name

    def getMotherName(self):
        return self.mothername 


class Children(Father, Mother):
    def __init__(self,name, fathername, mothername):
        Father.__init__(self,fathername)
        Mother.__init__(self,mothername)
        self.name = name

    def description(self):
        print(f'Hello, my name is {self.name} and i am a child of {self.fathername} and {self.mothername}')


father = Father('Mark')
mother = Mother('Sonia')
child = Children('John', father.getFatherName(), mother.getMotherName())
# child.description()      
child2 = Children('Bala','Lukka','Mano')
child2.description()      
print(child2.getFatherName())

"""
In multiple inheritances, the child class first searches for the method in its own class. If not found, then it searches in the parent classes depth_first and left-right order. Since this was an easy example with just two parent classes, we can clearly see that class Parent_1 was inherited first, so the child class will search the method in Parent_1 class before searching in class Parent_2.

But for complicated inheritance problems, it gets tough to identify the order. So the actual way of doing this is called Method Resolution Order (MRO) in Python. We can find the MRO of any class using the attribute __mro__.
"""

print(Children.__mro__)