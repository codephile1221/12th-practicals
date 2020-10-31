import mysql.connector
import sys
mydb=mysql.connector.connect(host='localhost',user='root',passwd='nazish123')
mycursor=mydb.cursor()
if mydb.is_connected()==False:
    print('Connection wasnt established')
    sys.exit()
try:
    mycursor.execute('create database Employee')
    mycursor.execute('use Employee')
except:
    print('Database already exists')

try:
    mycursor.execute('''create table Emp(Empno int(3) primary key,
                    Empname varchar(20) not null,Salary int(10),
                    Department varchar(20),Designation varchar(20))''')
except:
    print('Table already exists')
    sys.exit()
def Insert_Initial():
    rec=[]
    for I in range(6):
        no=int(input('Enter the employee no.='))
        name=input('Enter the employee name=')
        sal=float(input('Enter the employee salary='))
        dept=input('Enter the name of department=')
        desig=input("Enter designation=")
        X=(no,name,sal,dept,desig)
        rec.append(X)
    mycursor.executemany('insert into emp(empno,empname,salary,department,designation) values(%s,%s,%s,%s,%s)',rec)
    print(mycursor.rowcount,'rows affected')
    mydb.commit()
Insert_Initial()

def menu():
    while True:
        print(''' MENU
1. Add record
2. Search record
3. Update record
4. Delete record''')
        ch=int(input('Enter your choice='))
        if ch==1:
            addrecord()
        elif ch==2:
            searchrecord()
        elif ch==3:
            updaterecord()
        elif ch==4:
            deleterecord()
    else:
        print('Invalid choice')
        sys.exit()

def addrecord():
    no=int(input('Enter the employee no.='))
    name=input('Enter the employee name=')
    sal=float(input('Enter the employee salary='))
    dept=input('Enter the name of department=')
    desig=input("Enter designation=")
    X=(no,name,sal,dept,desig)
    command='insert into emp values(%s,%s,%s,%s,%s)'
    mycursor.execute(command,X)
    mydb.commit()
    print('Employee added')
    

def searchrecord():
    try:
        salary=int(input('Enter the salary ='))
        dep=input('Enter the dept=')
        X=(salary,dep)
        com='select * from emp where salary>%s and department=%s'
        mycursor.execute(com,X)
        records=mycursor.fetchall()
        for I in records:
            print(I)
    except:
        print('Records not found')
  

def updaterecord():
    empno=int(input('Employee no. to be updated='))
    command='update emp set salary=salary+0.35*salary where empno=%s'
    try:
        val=(empno,)
        mycursor.execute(command,val)
        mydb.commit()
        print('Record updated')
    except:
        print('Record not found')
    

def deleterecord():
    empn=int(input('Enter the emp no.='))
    try:
        comm='delete from emp where empno=%s'
        val=(empn,)
        mycursor.execute(comm,val)
        mydb.commit()
        print('Record deleted')
    except:
        print('Record not found')
    

menu()
