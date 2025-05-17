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
![image](https://github.com/user-attachments/assets/eb3e12f4-0cfd-4ad7-bca3-e1c8ddcf2b9d)

employee table
![image](https://github.com/user-attachments/assets/7cbb09f8-e59c-4375-b506-b7ba35e91647)

food table
![image](https://github.com/user-attachments/assets/2bb993b2-7aa0-4363-a12c-8b48c9eac30a)

orderfood table
![image](https://github.com/user-attachments/assets/9d308f3b-849f-4443-b4d0-83276b662774)

fee table
![image](https://github.com/user-attachments/assets/f022eeef-0d8b-4698-be40-908a94ac4390)

💡 Modify table structures as needed to suit your requirements.

💡 How to Use
Clone the repository or download the Python file.

Update the database credentials in the script:

![image](https://github.com/user-attachments/assets/c183364c-43ce-4458-8c21-9d589d0c3555)

Run the script:

![image](https://github.com/user-attachments/assets/a9bcc148-9ef0-484d-9b4b-e601a5b93a60)

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

![image](https://github.com/user-attachments/assets/a2c8aedf-facf-4101-ab1f-f21ec8e705bb)

to

![image](https://github.com/user-attachments/assets/60289cf4-9b72-4369-b4b8-540de4db7fac)

📌 To-Do / Improvements
Add validation for user inputs

Encrypt passwords for employee accounts

Add login authentication

Enhance error handling

Add GUI (Tkinter or PyQt) for better user experience
