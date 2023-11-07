
# database connection in python

import mysql.connector


def CreateCon():
    return mysql.connector.connect(user = 'root',
                                   host = 'localhost',
                                   database = 'python',
                                   password = '')

# create table
'''
def CreateTab():
    conn = CreateCon()
    cursor = conn.cursor() #help to execute queary
    query = "create table student(sid INT primary key auto_increment,name VARCHAR(30), email VARCHAR(30), city VARCHAR(30))"
    cursor.execute(query)
    conn.commit()
    print("Created Table")
    conn.close()

CreateTab()
'''
# Insert Data into Table 

'''
def InsertData(name,email,city):
    conn = CreateCon()
    cursor = conn.cursor()
    
    query = "insert into student(name,email,city) values(%s,%s,%s)"
    values = (name,email,city)
    cursor.execute(query,values)
    conn.commit()
    print("Inserted Data")
    conn.close()

n = input("Enter Name : ")
e = input("Enetr Email : ")
c = input("Enter City : ")

InsertData(n,e,c)
'''

# fetch data from database


def ShowData():
    conn = CreateCon()
    cursor = conn.cursor()

    query = "select * from student"

    cursor.execute(query)
    result = cursor.fetchall()
    for i in result: 
        print(i)
    
ShowData()


# Fetch data from table by Id

'''
def ShowDataId(sid):
    conn = CreateCon()
    cursor = conn.cursor()

    
    query = "select * from student where sid=%s"
    values = (sid,)
    cursor.execute(query,values)
    res = cursor.fetchall()
    for i in res:
        print(i)

ShowData()

sid = int(input("Enter Id : "))
ShowDataId(sid)
'''

# update data into database

'''
def UpdateData(name,email,city,sid):
    conn = CreateCon()
    cursor = conn.cursor()

    query = "update student set name=%s,email=%s,city=%s where sid=%s"
    values = (name,email,city,sid)

    cursor.execute(query,values)
    conn.commit()
    print("Data Updated")
    conn.close()


sid = int(input("Enter Id : "))

n = input("Enter Name : ")
e = input("Enter Email : ")
c = input("Enter City : ")

UpdateData(n,e,c,sid)

ShowData()
'''

# Delete Data from Database

def DeleteData(sid):
    conn = CreateCon()
    cursor = conn.cursor()

    query = "delete from student where sid=%s"

    values = (sid,)
    cursor.execute(query,values)
    conn.commit()
    print("Deleted Data ")
    conn.close()

sid = int(input("Enter Id : "))

DeleteData(sid)

ShowData()
    








    

