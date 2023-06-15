#single inheritance

class Parent:

    def fun1(self):
        print("This is Parent class")

class Child(Parent):

    def fun2(self):
        print("This is Child class")

obj=Child()
obj.fun1()
obj.fun2()
