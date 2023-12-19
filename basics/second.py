class Person:
    def __init__(self, name, age, profession):
        self.name = name
        self.age = age
        self.profession = profession


    def getFullData(self):
        return f'Name: {self.name}\nAge: {self.age}\nProfession: {self.profession}'
    
rohan = Person("Rohan Adnan", 21, "Web Developer")
print(rohan.getFullData())    
print("--------------------------------------------------")
laiba = Person("Laiba Khan", 18, "Student")
print(laiba.getFullData())

