d={}
while True:
    print("Menu")
    print(" 1. Display Contact \n 2. Add Contact \n 3. Delete Contact \n 4. Change Contact No. \n 5. Search Contact \n 6. Exist")

    n=int(input("Enter your Choice : "))

    if n==1:
        print("Saved Contact Number")
        for i in d:
            print("Name : ",i)
            print("Phone Number : ",d[i])
            print("---------------")
    elif n==2:
        print("Add Contact Number ")
        name=input("Enter Name  :")
        ph=input("Enter Phone Number : ")
        #d[name]=ph
        d.setdefault(name,ph)
        print("Contact Saved.....")
    elif n==3:
        print("Delete Contact Number")
        nam=input("Enter name for delete : ")
        d.pop(nam)
        print("Contact Deleted Successfully ...")
    elif n==4:
        print("Change Contact Number")
        nam=input("Enter Name For Change Number : ")
        new_ph=input("Enter New Phone Number : ")
        d[nam]=new_ph
        print("Phone Number Change Successfully...")
    elif n==5:
        print("Search Contact Number")
        nam=input("Enter Name For Search : ")
        if nam in d:
            print("Record Found ",d[nam])
        else:
            print("Record Not Found...")
    elif n==6:

        input("Press Enter for Exis")
        break