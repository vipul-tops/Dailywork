
#hierarchical inheritance

class Teacher:

    def teacher(self):
        print("This is Teacher")
      

class Student1(Teacher):

    def student(self):
        print("This is Student1")
       


class Student2(Teacher):

    def student2(self):
        print("This Is Student2")
        

obj=Student1()
obj2=Student2()

obj.teacher()
obj.student()

obj2.teacher()
obj2.student2()
