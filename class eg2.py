class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def __str__(self):
        return f"{self.name}{self.age}"

c1=Person("Vipul ","24")
print(c1)

