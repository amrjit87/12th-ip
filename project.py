import mysql.connector
from datetime import datetime
# print("connected!!")

con= mysql.connector.connect(host='localhost',user='root',password='Amarjit@87')

cur=con.cursor()
cur.execute("CREATE DATABASE if not exists bakery")
cur.execute("USE bakery")
cur.execute("CREATE TABLE if not exists cs(itm_no int,products varchar(20),cost int)")
query_1= "select*from cs"
cur.execute(query_1)
res=cur.fetchall()
if res==[]:
    cur.execute("insert into cs values(01,'coke',40)")
    cur.execute("insert into cs values(02,'cake',150)")
    cur.execute("insert into cs values(03,'pepsi',40)")
    cur.execute("insert into cs values(04,'samosa',20)")
    cur.execute("insert into cs values(05,'pastry',30)")
    cur.execute("insert into cs values(06,'patties',15)")
    cur.execute("insert into cs values(07,'pizza',120)")
    cur.execute("insert into cs values(08,'burger',50)")
    cur.execute("insert into cs values(09,'popcorn',80)")
    cur.execute("insert into cs values(10,'water',20)")
    cur.execute("insert into cs values(11,'chips small',10)")
    cur.execute("insert into cs values(12,'fries',80)")
    cur.execute("insert into cs values(13,'chips medium',25)")
    cur.execute("insert into cs values(14,'chips large',40)")
    con.commit()
# print("added succesfully!!!")  


cur.execute("CREATE TABLE if not exists empy(emp_no varchar(20),emp_name varchar(20),emp_role varchar(20),emp_salary int,emp_DOJ int)")
query_2= "select*from empy"
cur.execute(query_2)
res=cur.fetchall()
if res==[]:
   cur.execute("insert into empy values('A21M0','Mukesh Kumar','accountant',24000,2021)")
   cur.execute("insert into empy values('T19A0','Ashish Kumar','table man',19000,2019)")
   cur.execute("insert into empy values('M19S0','Suresh Kumar','manager',38000,2019)")
   cur.execute("insert into empy values('A22H0','Hamid','accontant',24000,2022)")
   cur.execute("insert into empy values('C23A0','Abdul' ,'cleaner',14000,2023)")
   cur.execute("insert into empy values('C21J0','Jiya Kumari','cook',26000,2021)")
   cur.execute("insert into empy values('C22M0','Manish Kumar','cook',26000,2022)")
   cur.execute("insert into empy values('C21S0','Surendra Kumar','cleaner',14000,2021)")
   con.commit()
# print("added_succesfully!!!")
   
# print("______________________CLASS 12th IP PROJECT 2023_____________________________")
# print("____________________________@@WELCOME@@______________________________________")
print(''' PLEASE CHOOSE 
1 FOR ADMIN
2 FOR CUSTOMER
3 EMPY
4 EXIT''')

val = int(input("Enter your value: "))
if val==1:
    print("!! _____FILL THE DETAILS_____!!")
    user= input("Enter your User name:")

    pass_word = input ("Enter your pasword:")

    if  pass_word=="Login@11":
        print("YOU LOGGED IN AS ADMIN")
        

    
        



        








    









 
