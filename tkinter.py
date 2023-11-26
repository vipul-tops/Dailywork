# tkinter

from tkinter import *
import mysql.connector
import tkinter.messagebox as msg

#creating main window

r = Tk()
r.geometry("250x250")
r.configure(bg="Light Blue")
r.title("My Title")

def CreateCon():
    return mysql.connector.connect(user = 'root',
                                   host = 'localhost',
                                   database = 'tkinter',
                                   password = '')

# Insert Data

def InsertData():
    rno = ern.get()
    na = en.get()
    ema = eem.get()
    mo = em.get()

    if (rno=="" or na=="" or ema=="" or mo==""):
        msg.showinfo("insert Status", "All Field Mandatory")
    else:
        try:
            conn = CreateCon()
            cursor = conn.cursor()
            args = (rno,na,ema,mo)
            query = "insert into student(rollno,name,email,mobile) values(%s,%s,%s,%s)"
            cursor.execute(query,args)
            conn.commit()
            msg.showinfo("Alert", "Data Inserted")
            conn.close()
        except Exception as ee:
            print("Insert Exception : ",ee)

def Update():
    rno = ern.get()
    na = en.get()
    ema = eem.get()
    mo = em.get()
  
   if(na == "" or ema == "" or mo == ""):
       msg.showinfo("ALERT", "Please enter fiels you want to update!")
   else:
       conn = CreateCon()
       cursor = conn.cursor()
       cursor.execute("update Person set name = '"+ name +"', phone='"+ phone +"' where id ='"+ id +"'")
       cursor.execute("commit");
  
       msg.showinfo("Status", "Successfully Updated")
       con.close();

# Adding Label in Main Window
rn = Label(r,text="Roll No")
rn.place(x = 20,y = 40)

n = Label(r,text="Name")
n.place(x = 20,y = 80)

e = Label(r,text="Email")
e.place(x = 20,y = 120)

m = Label(r,text="Mobile")
m.place(x = 20,y = 160)

# Adding Entry In Main Window

ern = Entry()
ern.place(x = 80,y = 40)

en = Entry()
en.place(x = 80,y = 80)

eem = Entry()
eem.place(x = 80,y = 120)

em = Entry()
em.place(x = 80,y = 160)

# Adding Button in Main Window

b1 = Button(r,text="Insert",bg="White",command=InsertData)
b1.place(x = 15, y = 200)

b2 = Button(r,text="Delete",bg="White")
b2.place(x = 62, y = 200)

b3 = Button(r,text="Update",bg="White")
b3.place(x = 115, y = 200)

b4 = Button(r,text="Delete",bg="White")
b4.place(x = 170, y = 200)

# mainloop method called

mainloop()
