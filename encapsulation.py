#Encapsulation

#Wrapping up data into single Unit
#data hiding

class Base:

    def __init__(self):
        self.a="Vipul"
        self.b="Memakiya"

class Derived(Base):
    def __init__(self):
        Base.__init__(self)
        print("Calling private member of base class :")
        print(self.b)

obj1=Base()
print(obj1.a)
            
