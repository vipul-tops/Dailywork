
#multilevel inheritance

class Grand:

    def __init__(self,grandf):
        self.grandf= grandf

class Father(Grand):

    def __init__(self,fathername,grandf):
        self.fathername= fathername

        Grand.__init__(self,grandf)

class Son(Father):

    def __init__(self,sonname,fathername,grandf):
        self.sonname= sonname

        Father.__init__(self,fathername,grandf)

    def display(self):

        print("Grand Father Name : ",self.grandf)
        print("Father Name : ",self.fathername)
        print("Son Name : ",self.sonname)

s1=Son("Magal","Chhagan","Chaku")
s1.display()
