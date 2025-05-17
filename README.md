# Food-Booking-System
Database Management System (DBMS) Project

This is a simple console-based Food Ordering System built with Python and MySQL. It supports basic CRUD operations for managing Customers, Employees, Food Items, Orders, and Payments.

🚀 Features
Add new Employees, Customers, and Food Items

Place Food Orders

View details of Customers, Employees, Orders, and Food Items

Manage Payment details

Optionally print order bills

Simple menu-driven interface

🧰 Tech Stack
Language: Python 3.x

Database: MySQL

Library Used: mysql-connector-python

🛠️ Setup Instructions
1. Prerequisites
Python installed on your system

MySQL installed and running

mysql-connector-python installed
Install it using pip:

![image](https://github.com/user-attachments/assets/9c3c8a00-97c7-40e4-8c64-0c53e1396d3e)

2. Database Configuration
Make sure your MySQL database (csproject) includes the following tables:

customer table
sql
Copy
Edit
CREATE TABLE customer (
  cust_id INT PRIMARY KEY,
  name VARCHAR(100),
  phone BIGINT,
  payment INT,
  stat VARCHAR(50),
  email VARCHAR(100),
  orderid VARCHAR(50),
  date DATE
);
employee table
sql
Copy
Edit
CREATE TABLE employee (
  emp_id INT PRIMARY KEY,
  name VARCHAR(100),
  emp_g VARCHAR(10),
  age INT,
  emp_phone BIGINT,
  pwd VARCHAR(50)
);
food table
sql
Copy
Edit
CREATE TABLE food (
  food_id INT PRIMARY KEY,
  foodname VARCHAR(100),
  food_size VARCHAR(20),
  prize INT
);
orderfood table
sql
Copy
Edit
CREATE TABLE orderfood (
  order_id INT PRIMARY KEY,
  cust_id INT,
  emp_id INT,
  food_id INT,
  food_qty INT,
  total_price INT
);
fee table
sql
Copy
Edit
CREATE TABLE fee (
  roll INT,
  feedeposit INT,
  month VARCHAR(20)
);
💡 Modify table structures as needed to suit your requirements.

💡 How to Use
Clone the repository or download the Python file.

Update the database credentials in the script:

python
Copy
Edit
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="12345",
    database="csproject"
)
Run the script:

bash
Copy
Edit
python food_ordering_system.py
Follow the on-screen prompts to perform different operations.

📋 Menu Options
1 – Add Employee

2 – Add Customer

3 – Add Food

4 – Order Food

5 – Fee Deposit

6 – View Records

⚠️ Notes
Ensure your database is running before executing the program.

This script uses direct input() calls and lacks validations—handle with caution for production use.

The View function has a bug in Employee SQL query:
Change

sql
Copy
Edit
sql="select  from Employee where Emp_id=%s"
to

sql
Copy
Edit
sql="select * from Employee where Emp_id=%s"
📌 To-Do / Improvements
Add validation for user inputs

Encrypt passwords for employee accounts

Add login authentication

Enhance error handling

Add GUI (Tkinter or PyQt) for better user experience

📄 License
This project is free to use and modify for educational purposes.
