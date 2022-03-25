import pymysql

def showrecord_employee():
    conn = pymysql.connect(host = "localhost",user = "root", password = "", db = "ecom")
    cur = conn.cursor()
    cur.execute("SELECT * FROM `employee`")
    output = cur.fetchall()
    for x in output:
        print(x)


def showrecord_customer():
    conn = pymysql.connect(host = "localhost",user = "root", password = "", db = "ecom")
    cur = conn.cursor()
    cur.execute("SELECT * FROM `customer`")
    output = cur.fetchall()
    for x in output:
        print(x)
        

def insert_employee():
     conn = pymysql.connect(host = "localhost",user = "root", password = "", db = "ecom")
     name = input("Enter employee name: ")
     phone_number = input("Enter employee phone number: ")
     city = input("Enter employee city: ")
     insert_employee_sql = "INSERT INTO `employee` (`emp_id`, `emp_name`, `emp_phone_number`, `emp_city`) VALUES (NULL, '"+name+"', '"+phone_number+"', '"+city+"')"
     cur = conn.cursor()
     cur.execute(insert_employee_sql)
     conn.commit()
     print("Record inserted and employee table updated successfully")


def insert_customer():
     conn = pymysql.connect(host = "localhost", user = "root", password = "", db = "ecom")
     name = input("Enter customer name: ")
     phone_number = input("Enter customer phone number: ")
     city = input("Enter customer city: ")
     insert_customer_sql = "INSERT INTO `customer` (`cust_id`, `cust_name`, `cust_phone_number`, `cust_city`) VALUES (NULL, '"+name+"', '"+phone_number+"', '"+city+"')"
     cur = conn.cursor()
     cur.execute(insert_customer_sql)
     conn.commit()
     print("Record inserted and customer table updated successfully")
     

def update_employee():
     conn = pymysql.connect(host = "localhost",user = "root", password = "", db = "ecom")
     emp_id = int(input("Enter employee id: "))
     name = input("Enter employee name: ")
     phone_number = input("Enter employee phone number: ")
     city = input("Enter employee city: ")
     update_employee_sql = "UPDATE `employee` SET `emp_phone_number` = '"+phone_number+"', `emp_name` = '"+name+"', `emp_city` = '"+city+"' WHERE `employee`.`emp_id` = '"+str(emp_id)+"'"
     cur = conn.cursor()
     cur.execute(update_employee_sql)
     conn.commit()
     print(f"Employee with id {emp_id} updated")


def update_customer():
     conn = pymysql.connect(host = "localhost",user = "root", password = "", db = "ecom")
     cust_id = int(input("Enter customer id: "))
     name = input("Enter customer name: ")
     phone_number = input("Enter customer phone number: ")
     city = input("Enter customer city: ")
     update_customer_sql = "UPDATE `customer` SET `cust_phone_number` = '"+phone_number+"', `cust_name` = '"+name+"', `cust_city` = '"+city+"' WHERE `customer`.`cust_id` = '"+str(cust_id)+"'"
     cur = conn.cursor()
     cur.execute(update_customer_sql)
     conn.commit()
     print(f"Customer with id {cust_id} updated")
     

def delete_employee():
     conn = pymysql.connect(host = "localhost",user = "root", password = "", db = "ecom")
     emp_id = int(input("Enter employee id: "))
     delete_employee_sql = f"DELETE FROM `employee` WHERE `employee`.`emp_id` = '{emp_id}' "
     cur = conn.cursor()
     cur.execute(delete_employee_sql)
     conn.commit()
     print(f"Employee with id {emp_id} deleted")


def delete_customer():
     conn = pymysql.connect(host = "localhost",user = "root", password = "", db = "ecom")
     cust_id = int(input("Enter customer id: "))
     delete_customer_sql = f"DELETE FROM `customer` WHERE `customer`.`cust_id` = '{cust_id}' "
     cur = conn.cursor()
     cur.execute(delete_customer_sql)
     conn.commit()
     print(f"Customer with id {cust_id} deleted")
     

ch = 0
print("Welcome to Hemant's Python CRUD application")

while ch != 9:
    print("1) List of all records in employee table")
    print("2) List of all records in customer table")
    print("3) Insert into employee table")
    print("4) Insert into customer table")
    print("5) Update employee table")
    print("6) Update customer table")
    print("7) Delete from employee table")
    print("8) Delete from customer table")
    print("9) Exit")

    ch = int(input("Enter your choice: "))
    
    if ch == 1:
        showrecord_employee()
        
    if ch == 2:
        showrecord_customer()

    if ch == 3:
        insert_employee()
        print("Updated employee table: ")
        showrecord_employee()

    if ch == 4:
        insert_customer()
        print("Updated customer table: ")
        showrecord_customer()
        
    if ch == 5:
        update_employee()
        print("Updated employee table: ")
        showrecord_employee()

    if ch == 6:
        update_customer()
        print("Updated customer table: ")
        showrecord_customer()
        
    if ch == 7:
        delete_employee()
        print("Updated employee table: ")
        showrecord_employee()

    if ch == 8:
        delete_customer()
        print("Updated customer table: ")
        showrecord_customer()