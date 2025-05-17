import os
import platform
import mysql.connector
mydb=mysql.connector.connect(host="localhost",\
                             user="root",\
                             passwd ="12345",\
                             database="csproject")

mycursor=mydb.cursor()
def Customer():
    X=[]
    cust_id=int(input("Enter the customer ID number : "))
    X.append(cust_id)
    name=input("Enter the Customer Name: ")
    X.append(name)
    phone=int(input("Enter customer phone number : "))
    X.append(phone)
    payment=int(input("Enter payment method ((1)credit card/(2)Debit Card:) "))
    X.append(payment)
    stat=input("Enter the payment status : ")
    X.append(stat)
    email=input("Enter the email id")
    X.append(email)
    orderid=input("enter orderid")
    X.append(orderid)
    date=input("Enter Date  : ")
    X.append(date)
    cust=(X)
    sql="insert into customer (cust_id,name,phone,payment,stat,email,orderid,date) values (%s,%s,%s,%s,%s,%s,%s,%s)"
    mycursor.execute(sql,cust)
    mydb.commit()

def Employee():
    X=[]
    Emp_id=int(input("Enter the Employee id : "))
    X.append(Emp_id)
    name=input("Enter the Employee Name: ")
    X.append(name)
    emp_g=input("Enter Employee Gender : ")
    X.append(emp_g)
    age=int(input("Enter Employee age"))
    X.append(age)
    emp_phone=int(input("enter employee phone number"))
    X.append(emp_phone)
    pwd=input("Enter the password : ")
    X.append(pwd)
    EMP=(X)
    sql="insert into Employee (Emp_id,name,emp_g,age,emp_phone,pwd) values (%s,%s,%s,%s,%s,%s)"
    mycursor.execute(sql,EMP)
    mydb.commit()

def Food():
    X=[]
    Food_id=int(input("Enter the Food id : "))
    X.append(Food_id)
    Foodname=input("Enter the Food Name: ")
    X.append(Foodname)
    Food_size=input("Enter Food size : ")
    X.append(Food_size)
    Price =int(input("Enter Price of Food"))
    X.append(Price)
    Food=(X)
    sql="insert into Food (Food_id,Foodname,Food_size,prize ) values (%s,%s,%s,%s)"
    mycursor.execute(sql,Food)
    mydb.commit()			

def OrderFood():
    X=[]
    Order_id=int(input("Enter the Food Order id : "))
    X.append(Order_id)
    Cust_id=input("Enter the Customer id : ")
    X.append(Cust_id)
    Emp_id=input("Enter Employee id: ")
    X.append(Emp_id)
    Food_id=int(input("Enter Food id"))
    X.append(Food_id)
    Food_qty=input("Enter Qty: ")
    X.append(Food_qty)
    Total_price=input("Enter Total_price")
    X.append(Total_price)
    OrderFood=(X)
    sql="insert into OrderFood (Order_id,Cust_id,Emp_id,Food_id,Food_qty,Total_price ) values (%s,%s,%s,%s,%s,%s)"
    mycursor.execute(sql,OrderFood)

    n=int(input("DO YOU WANT TO PRINT THE BILL? \n If YES press 1 \n If No Press 2"))
    if(n==1):
        s= input("Enter Order id")
        rl=(s,)
        sql="select * from orderfood where order_id=%s"
        mycursor.execute(sql,rl)
        res=mycursor.fetchall()
        for x in res:
            print(x)
    
    
    elif(n==2):
        pass

    
    mydb.commit()


def  View():
    print("Select the search criteria : ") 
    print("1. Employee")
    print("2. Customer")
    print("3. Food")
    print("4. Order Food")
    ch=int(input("Enter the choice 1 to 4 : "))
    if (ch==1):
        s=int(input("enter Employee ID:"))
        rl=(s,)
        sql="select  from Employee where Emp_id=%s" 
        mycursor.execute(sql,rl)
        res=mycursor.fetchall()
        for x in res:
            print(x)

    elif (ch==2):
        s=input("Enter Customer Id : ")
        rl=(s,)
        sql="select * from Customer where cust_id=%s"
        mycursor.execute(sql,rl)
        res=mycursor.fetchall()
        for x in res:
            print(x)

    elif (ch==3):
        s= input("Enter Food id")
        rl=(s,)
        sql="select * from Food where food_id=%s"
        mycursor.execute(sql,rl)
        res=mycursor.fetchall()
        for x in res:
            print(x)


    elif (ch==4):
        s=int(input("Enter Food ID : "))
        rl=(s,)
        sql="select * from Orderfood where food_id=%s"
        mycursor.execute(sql,rl)
        res=mycursor.fetchall()
        for x in res:
            print(x)

def  Payment():
    X=[]
    roll=int(input("Enter the roll number : "))
    X.append(roll)
    feedeposit=int(input("Enter the Fee to be deposited : "))
    X.append(feedeposit)
    month=input("Enter month of fee : ")
    X.append(month)
    fee=(X)
    sql="insert into fee (roll,feedeposit,month) values (%s,%s,%s)"
    mycursor.execute(sql,fee)
    mydb.commit()




def Menu():
    print("Enter 1 : To Add Employee")
    print("Enter 2 : To Add Cutomer details")
    print("Enter 3 : To Add Food Details ")
    print("Enter 4 : For Food Order")
    print("Enter 5 : For feeDeposit")
    print("Enter 6 : To view Food booking")

    try:

        userInput = int(input("Please Select An Above Option: ")) 
    except ValueError:
        exit("\nHy! That's Not A Number") 
    else:
        print("\n") 
    if (userInput==1):
        Employee()
    elif (userInput==2):
        Customer()
    elif (userInput==3):
        Food()
    elif (userInput==4):
        OrderFood()
    elif (userInput==5):
        Payment()
    elif (userInput==6):
        View()

    else:
        print("Enter the correct choice. . . ")


def runAgain():
    runAgn=input("\n Do you want to run again Y/N")
    while runAgn.lower()=='y':
        if(platform.system()=="Windows"):
            print(os.system('cls'))
        else:
            print(os.system('clear'))
        Menu()
        runAgn=input("\nwant to run Againy/n")
        print("HAVE A NICE DAY")

Menu()
runAgain()
