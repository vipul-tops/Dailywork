class Person:

    def __init__(self,name,idno):
        self.name=name
        self.id=idno

    def display(self):
        print(self.name)
        print(self.id)

    
class Employee(Person):

    def __init__(self,name,idno,salary,post):
        self.salary=salary
        self.post=post

        Person.__init__(self,name,idno)

    def details(self):
        print("My name is :{} ".format(self.name))
        print("My Id is : {}".format(self.id))
        print("My Post is :{} ".format(self.post))
        print("Salary :{} ".format(self.salary))

a=Employee("Vipul","101","20000","Python Developer")

a.details()



        
