'''
Here, the class Child_1 inherits two classes – Parent_1 and Parent_2. The class Child_2 is also inheriting two classes – Parent_2 and Parent_3. Another class, Child_3, is inheriting three classes – Child_1, Child_2, and Parent_3.

Now, just by looking at this inheritance, it is quite hard to determine the Method Resolution Order for class Child_3. So here is the actual use of __mro__.
'''

# Again to remember mro is used to find the order of inheritance as we want to call any method from the parent class

class Parent_1:
    def __init__(self):
        self.name = 'Parent_1'

class Parent_2:
    def __init__(self):
        self.name = 'Parent_2'

class Parent_3:
    def __init__(self):
        self.name = 'Parent_3'

class Child_1(Parent_1,Parent_2):
    pass

class Child_2(Parent_2,Parent_3):
    pass

class Child_3(Child_1,Child_2,Parent_3):
    pass


print(Child_3.__mro__)