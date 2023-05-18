class Student:

    def getdata(self,fname,lname):
        self.f=fname
        self.l=lname
    def putdata(self):
        print('First Name: ',self.f)
        print('Last Name: ',self.l)

s1=Student()
s1.getdata('Vipul','Memakiya')
s1.putdata()
