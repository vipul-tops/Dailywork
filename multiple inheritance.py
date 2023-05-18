#multiple inheritance

class Father:
    fathername=""

    def fun1(self):
        print(self.fathername)

class Mother:
    mothername=""

    def fun2(self):
        print(self.mothername)

class Son(Father,Mother):

    def fun3(self):
        print("Father Name : ",self.fathername)
        print("Mother Name : ",self.mothername)

obj=Son()
obj.fathername="Maganbhai"
obj.mothername="Chakuben"
obj.fun3()











        
