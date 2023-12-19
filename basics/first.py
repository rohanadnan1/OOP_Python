class Name:
    firstName = ""
    lastName = ""
    def getFullName(self, firstName, lastName):
        return firstName + " " + lastName
    
rohan = Name()
rohan.firstName = "Rohan"
rohan.lastName = "Adnan"
print(rohan.getFullName(rohan.firstName, rohan.lastName))