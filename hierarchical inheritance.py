
#hierarchical Inheritance

class Parent:

    def father(self):
        print("This is Parent class")

class Child(Parent):

    def son(self):
        print("This Is Child 1")

class Child2(Parent):

    def son2(self):
        print("This is Child 2")

obj1=Child()
obj2=Child2()

obj1.father()
obj1.son()

obj2.father()
obj2.son2
