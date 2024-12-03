print("Pham Tuan Dat")
print("235752021610105")
class Person:
    def __init__(self, name):
        self.name = name 
    def getGender(self):
        raise NotImplementedError("The getGender method needs to be defined in the subclass")
class Nam(Person):
    def __init__(self, name):
        super().__init__(name) 

    def getGender(self):
        return "Nam"
class Nữ(Person):
    def __init__(self, name):
        super().__init__(name)

    def getGender(self):
        return "Nữ"
    
Nam = Nam("Thanh")
Nữ = Nữ("NANH")
print(f"{Nam.name} là {Nam.getGender()}.")  
print(f"{Nữ.name} là {Nữ.getGender()}.") 

