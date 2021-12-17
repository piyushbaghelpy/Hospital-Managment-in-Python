#For admin window
def admin():
    print("\n\t***********************************************")
    print("\n\t************WELCOME TO PIYUSH HOSPITAL**********")
    print("\n\t***********************************************")
    a=input("enter password ")
    file=open("admin.txt",'r')
    q=file.read()    
    while True:
        if a==q:
            print("\n\t\t-------Welcome to admin window-------")
            print("\n***Admin Options***")
            q1=int(input("Press 1 to manage Doctor\nPress 2 to manage Patient\nPress 3 to manage Appoinment\nPress 4 to Change Password\n"))
            if q1==1:
                doctor()
            elif q1==2:
                patient()
            elif q1==3:
                appoinment()
            elif q1==4:
                changepass()              
                
            else:
                print("wrong choice")
                
        else:
            print("Wrong password try again")
            cont=input("press any key to continue")
            return

#For (admin then => doctor) 

def doctor():
    while True:
        print("\n\t\t-------Welcome to Doctor Managment Window-------")
        print("\n***Doctor Managment Options***")
        ch=int(input("Press 1 to display Doctors detail\nPress 2 to add Doctors\nPress 3 to Delete Doctors\nPress 4 to Edit Doctors info\nPress 5 to Return"))
        if ch==1:
            disdoc()
        elif ch==2:
            adddoc()
        elif ch==3:
            deldoc()
        elif ch==4:
            editdoc()
        elif ch==5:
            return
        else:
            print("\n-X-X-X-X-X-Wrong Choice Try Again-X-X-X-X-X-\n")
def disdoc():
    import mysql.connector
    mycon=mysql.connector.connect(host='localhost',user='root',passwd='piyush',database='hospital')
    cur=mycon.cursor()
    cur.execute("select*from doctor")
    row=cur.fetchall()
    for c in row:
        print(c)
    mycon.close()

def adddoc():
    id=int(input("enter doctors id"))
    name=(input("enter doctors name"))
    gender=(input("enter doctors gender"))
    department=(input("enter doctors department"))
    salary=int(input("enter doctors salary"))
    phone=int(input("enter doctors phone number"))
    address=(input("enter doctors address")) 
    import mysql.connector
    mycon=mysql.connector.connect(host='localhost',user='root',passwd='piyush',database='hospital')
    cur=mycon.cursor()
    insert="insert into doctor(id,name,gender,department,salary,phone_no,address)values({},'{}','{}','{}',{},{},'{}')".format(id,name,gender,department,salary,phone,address)
    cur.execute(insert)
    mycon.commit()
    mycon.close()
    print("Record has been saved")
    

def deldoc():
    id=int(input("enter doctors id which you want to delete"))
    import mysql.connector
    mycon=mysql.connector.connect(host='localhost',user='root',passwd='piyush',database='hospital')
    cur=mycon.cursor()
    dele="delete from doctor where id='{}'".format(id)
    cur.execute(dele)
    mycon.commit()
    mycon.close()
    print("id number",id,"Record has been deleted")

def editdoc():
    ch=int(input("\nPress 1 to edit name\nPress 2 to edit gender\nPress 3 to edit department\nPress 4 to edit salary\nPress 5 to edit phone number\nPress 6 to edit address"))
    import mysql.connector
    mycon=mysql.connector.connect(host='localhost',user='root',passwd='piyush',database='hospital')
    if ch==1:
        edname()
    elif ch==2:
        edgender()
    elif ch==3:
        eddepartment()
    elif ch==4:
        edsalary()
    elif ch==5:
        edphone()
    elif ch==6:
        edaddress()
    else:
        return

def edname():
    import mysql.connector
    mycon=mysql.connector.connect(host='localhost',user='root',passwd='piyush',database='hospital')
    cur=mycon.cursor()
    name=input("enter the name")
    id=int(input("enter the id of the person that name should be change"))
    edit="update doctor set name='{}' where id ={}".format(name,id)
    cur.execute(edit)
    mycon.commit()
    mycon.close()
    print("Record has been edited")

def eddepartment():
    import mysql.connector
    mycon=mysql.connector.connect(host='localhost',user='root',passwd='piyush',database='hospital')
    cur=mycon.cursor()
    department=input("enter the department")
    id=int(input("enter the id of the person that department should be change"))
    edit="update doctor set department='{}' where id ={}".format(department,id)
    cur.execute(edit)
    mycon.commit()
    mycon.close()
    print("Record has been edited")

def edsalary():
    import mysql.connector
    mycon=mysql.connector.connect(host='localhost',user='root',passwd='piyush',database='hospital')
    cur=mycon.cursor()
    salary=input("enter the salary")
    id=int(input("enter the id of the person that salary should be change"))
    edit="update doctor set salary='{}' where id ={}".format(salary,id)
    cur.execute(edit)
    mycon.commit()
    mycon.close()
    print("Record has been edited")


def edgender():
    import mysql.connector
    mycon=mysql.connector.connect(host='localhost',user='root',passwd='piyush',database='hospital')
    cur=mycon.cursor()
    gender=input("enter the gender")
    id=int(input("enter the id of the person that gender should be change"))
    edit="update doctor set gender='{}' where id ={}".format(gender,id)
    cur.execute(edit)
    mycon.commit()
    mycon.close()
    print("Record has been edited")

def edphone():
    import mysql.connector
    mycon=mysql.connector.connect(host='localhost',user='root',passwd='piyush',database='hospital')
    cur=mycon.cursor()
    phone=input("enter the phone")
    id=int(input("enter the id of the person that phone should be change"))
    edit="update doctor set phone_no='{}' where id ={}".format(phone,id)
    cur.execute(edit)
    mycon.commit()
    mycon.close()
    print("Record has been edited")

def edaddress():
    import mysql.connector
    mycon=mysql.connector.connect(host='localhost',user='root',passwd='piyush',database='hospital')
    cur=mycon.cursor()
    address=input("enter the address")
    id=int(input("enter the id of the person that address should be change"))
    edit="update doctor set address='{}' where id ={}".format(address,id)
    cur.execute(edit)
    mycon.commit()
    mycon.close()
    print("Record has been edited")

#For (admin then => patient)
    
def patient():
    while True:
        print("\n\t\t-------Welcome to patient Managment Window-------")
        print("\n***Patient Managment Options***")
        ch=int(input("Press 1 to display Patient detail\nPress 2 to add Patients\nPress 3 to Delete Patients\nPress 4 to Edit Patients info\nPress 5 to Return"))
        if ch==1:
            dispat()
        elif ch==2:
            addpat()
        elif ch==3:
            delpat()
        elif ch==4:
            editpat()
        elif ch==5:
            return
        else:
            print("\n-X-X-X-X-X-Wrong Choice Try Again-X-X-X-X-X-\n")

def dispat():
    import mysql.connector
    mycon=mysql.connector.connect(host='localhost',user='root',passwd='piyush',database='hospital')
    cur=mycon.cursor()
    cur.execute("select*from patient")
    row=cur.fetchall()
    for c in row:
        print(c)
    mycon.close()


def addpat():
    id=int(input("enter patient id"))
    name=(input("enter patient name"))
    gender=(input("enter patient gender"))
    age=(input("enter patient age"))
    phone=int(input("enter patient phone number"))
    address=(input("enter patient address"))
    disease=(input("enter patient disease"))
    date=(input("enter todays date"))
    appoint=(input("enter patient's doctor appoint"))
    
    import mysql.connector
    mycon=mysql.connector.connect(host='localhost',user='root',passwd='piyush',database='hospital')
    cur=mycon.cursor()
    insert="insert into patient(id,name,gender,age,phone_no,address,disease,date,doctor_appoint)values({},'{}','{}',{},{},'{}','{}','{}','{}')".format(id,name,gender,age,phone,address,disease,date,appoint)
    cur.execute(insert)
    mycon.commit()
    mycon.close()
    print("Record has been saved")
    

def delpat():
    id=int(input("enter patient id which you want to delete"))
    import mysql.connector
    mycon=mysql.connector.connect(host='localhost',user='root',passwd='piyush',database='hospital')
    cur=mycon.cursor()
    dele="delete from patient where id='{}'".format(id)
    cur.execute(dele)
    mycon.commit()
    mycon.close()
    print("id number",id,"Record has been deleted")

def editpat():
    ch=int(input("\nPress 1 to edit name\nPress 2 to edit gender\nPress 3 to edit age\nPress 4 to edit phone number\nPress 5 to edit address\nPress 6 to edit disease\nPress 7 to edit date\nPress 8 to edit doctor appoint"))
    import mysql.connector
    mycon=mysql.connector.connect(host='localhost',user='root',passwd='piyush',database='hospital')
    if ch==1:
        ediname()
    elif ch==2:
        edigender()
    elif ch==3:
        ediage()
    elif ch==4:
        ediphone()
    elif ch==5:
        ediaddress()
    elif ch==6:
        edidisease()
    elif ch==7:
        edidate()
    elif ch==8:
        ediappoint()
    else:
        return

def ediname():
    import mysql.connector
    mycon=mysql.connector.connect(host='localhost',user='root',passwd='piyush',database='hospital')
    cur=mycon.cursor()
    name=input("enter the name")
    id=int(input("enter the id of the person that name should be change"))
    edit="update patient set name='{}' where id ={}".format(name,id)
    cur.execute(edit)
    mycon.commit()
    mycon.close()
    print("Record has been edited")

def edigender():
    import mysql.connector
    mycon=mysql.connector.connect(host='localhost',user='root',passwd='piyush',database='hospital')
    cur=mycon.cursor()
    gender=input("enter the gender")
    id=int(input("enter the id of the person that gender should be change"))
    edit="update patient set gender='{}' where id ={}".format(gender,id)
    cur.execute(edit)
    mycon.commit()
    mycon.close()
    print("Record has been edited")
def ediage():
    import mysql.connector
    mycon=mysql.connector.connect(host='localhost',user='root',passwd='piyush',database='hospital')
    cur=mycon.cursor()
    age=input("enter the age")
    id=int(input("enter the id of the person that age should be change"))
    edit="update patient set age='{}' where id ={}".format(age,id)
    cur.execute(edit)
    mycon.commit()
    mycon.close()
    print("Record has been edited")
def ediphone():
    import mysql.connector
    mycon=mysql.connector.connect(host='localhost',user='root',passwd='piyush',database='hospital')
    cur=mycon.cursor()
    phone=input("enter the phone")
    id=int(input("enter the id of the person that phone number should be change"))
    edit="update patient set phone_no='{}' where id ={}".format(phone,id)
    cur.execute(edit)
    mycon.commit()
    mycon.close()
    print("Record has been edited")

def ediaddress():
    import mysql.connector
    mycon=mysql.connector.connect(host='localhost',user='root',passwd='piyush',database='hospital')
    cur=mycon.cursor()
    address=input("enter the address")
    id=int(input("enter the id of the person that address should be change"))
    edit="update patient set address='{}' where id ={}".format(address,id)
    cur.execute(edit)
    mycon.commit()
    mycon.close()
    print("Record has been edited")

def edidisease():
    import mysql.connector
    mycon=mysql.connector.connect(host='localhost',user='root',passwd='piyush',database='hospital')
    cur=mycon.cursor()
    disease=input("enter the disease")
    id=int(input("enter the id of the person that disease should be change"))
    edit="update patient set disease='{}' where id ={}".format(disease,id)
    cur.execute(edit)
    mycon.commit()
    mycon.close()
    print("Record has been edited")

def edidate():
    import mysql.connector
    mycon=mysql.connector.connect(host='localhost',user='root',passwd='piyush',database='hospital')
    cur=mycon.cursor()
    date=input("enter the date")
    id=int(input("enter the id of the person that date should be change"))
    edit="update patient set date='{}' where id ={}".format(date,id)
    cur.execute(edit)
    mycon.commit()
    mycon.close()
    print("Record has been edited")

def ediappoint():
    import mysql.connector
    mycon=mysql.connector.connect(host='localhost',user='root',passwd='piyush',database='hospital')
    cur=mycon.cursor()
    appoint=input("enter the doctor appoint")
    id=int(input("enter the id of the person that date should be change"))
    edit="update patient set doctor_appoint='{}' where id ={}".format(appoint,id)
    cur.execute(edit)
    mycon.commit()
    mycon.close()
    print("Record has been edited")

#For (admin then => appoinment)
def appoinment():
    while True:
        print("\n\t\t-------Welcome to Appoinment Window-------")
        print("\n***Appoinment Options***")
        ch=int(input("Press 1 to display appoinments\nPress 2 to book appoinment\nPress 3 to edit appoinment\nPress 4 to Cancel appoinment\nPress 5 to Return"))
        if ch==1:
            bdisplay()
        elif ch==2:
            bbook()
        elif ch==3:
            bedit()
        elif ch==4:
            bcancel()
        elif ch==5:
            return
        else:
            print("\n-X-X-X-X-X-Wrong Choice Try Again-X-X-X-X-X-\n")

def bdisplay():
    import mysql.connector
    mycon=mysql.connector.connect(host='localhost',user='root',passwd='piyush',database='hospital')
    cur=mycon.cursor()
    cur.execute("select*from appoinment")
    row=cur.fetchall()
    for c in row:
        print(c)
    mycon.close()

def bbook():
    id=int(input("enter appoinment id"))
    date_appoint=(input("enter the date appoint"))
    client_id=int(input("enter client id"))
    client_name=(input("enter client name"))
    client_contact=int(input("enter client contact number"))
    start_time=(input("enter starting time"))
    end_time=(input("enter ending time"))
    doctor_name=(input("enter doctor's name"))
    
    import mysql.connector
    mycon=mysql.connector.connect(host='localhost',user='root',passwd='piyush',database='hospital')
    cur=mycon.cursor()
    insert="insert into appoinment(id,date_appoint,client_id,client_name,client_contact,start_time,end_time,doctor_name)values({},'{}',{},'{}',{},'{}','{}','{}')".format(id,date_appoint,client_id,client_name,client_contact,start_time,end_time,doctor_name)
    cur.execute(insert)
    mycon.commit()
    mycon.close()
    print("Record has been saved")

def bedit():
    ch=int(input("\nPress 1 to edit appointment date\nPress 2 to edit client id\nPress 3 to edit client name\nPress 4 to edit client contact number\nPress 5 to edit start time\nPress 6 to edit end time\nPress 7 to edit doctor's name"))
    import mysql.connector
    mycon=mysql.connector.connect(host='localhost',user='root',passwd='piyush',database='hospital')
    if ch==1:
        editadate()
    elif ch==2:
        editcid()
    elif ch==3:
        editcname()
    elif ch==4:
        editccontact()
    elif ch==5:
        editstime()
    elif ch==6:
        editetime()
    elif ch==7:
        editdname()
    else:
        return

def editadate():
    import mysql.connector
    mycon=mysql.connector.connect(host='localhost',user='root',passwd='piyush',database='hospital')
    cur=mycon.cursor()
    date=input("enter the date ")
    id=int(input("enter the id of the appointment"))
    edit="update appoinment set date_appoint='{}' where id ={}".format(date,id)
    cur.execute(edit)
    mycon.commit()
    mycon.close()
    print("Record has been edited")

def editcid():
    import mysql.connector
    mycon=mysql.connector.connect(host='localhost',user='root',passwd='piyush',database='hospital')
    cur=mycon.cursor()
    cid=input("enter the client id ")
    id=int(input("enter the id of the appointment"))
    edit="update appoinment set client_id='{}' where id ={}".format(cid,id)
    cur.execute(edit)
    mycon.commit()
    mycon.close()
    print("Record has been edited")
    
def editcname():
    import mysql.connector
    mycon=mysql.connector.connect(host='localhost',user='root',passwd='piyush',database='hospital')
    cur=mycon.cursor()
    name=input("enter the client name ")
    id=int(input("enter the id of the appointment"))
    edit="update appoinment set client_name='{}' where id ={}".format(name,id)
    cur.execute(edit)
    mycon.commit()
    mycon.close()
    print("Record has been edited")    
    
def editcname():
    import mysql.connector
    mycon=mysql.connector.connect(host='localhost',user='root',passwd='piyush',database='hospital')
    cur=mycon.cursor()
    name=input("enter the client name ")
    id=int(input("enter the id of the appointment "))
    edit="update appoinment set client_name='{}' where id ={}".format(name,id)
    cur.execute(edit)
    mycon.commit()
    mycon.close()
    print("Record has been edited")

def editccontact():
    import mysql.connector
    mycon=mysql.connector.connect(host='localhost',user='root',passwd='piyush',database='hospital')
    cur=mycon.cursor()
    con=input("enter the client contact number ")
    id=int(input("enter the id of the appointment "))
    edit="update appoinment set client_contact='{}' where id ={}".format(con,id)
    cur.execute(edit)
    mycon.commit()
    mycon.close()
    print("Record has been edited")

def editstime():
    import mysql.connector
    mycon=mysql.connector.connect(host='localhost',user='root',passwd='piyush',database='hospital')
    cur=mycon.cursor()
    stime=input("enter the start time ")
    id=int(input("enter the id of the appointment "))
    edit="update appoinment set start_time='{}' where id ={}".format(stime,id)
    cur.execute(edit)
    mycon.commit()
    mycon.close()
    print("Record has been edited")

def editetime():
    import mysql.connector
    mycon=mysql.connector.connect(host='localhost',user='root',passwd='piyush',database='hospital')
    cur=mycon.cursor()
    etime=input("enter the end time ")
    id=int(input("enter the id of the appointment "))
    edit="update appoinment set end_time='{}' where id ={}".format(etime,id)
    cur.execute(edit)
    mycon.commit()
    mycon.close()
    print("Record has been edited")


def editdname():
    import mysql.connector
    mycon=mysql.connector.connect(host='localhost',user='root',passwd='piyush',database='hospital')
    cur=mycon.cursor()
    ename=input("enter the doctor's name ")
    id=int(input("enter the id of the appointment "))
    edit="update appoinment set doctor_name='{}' where id ={}".format(ename,id)
    cur.execute(edit)
    mycon.commit()
    mycon.close()
    print("Record has been edited")

def bcancel():
    import mysql.connector
    mycon=mysql.connector.connect(host='localhost',user='root',passwd='piyush',database='hospital')
    cur=mycon.cursor()
    cancel=int(input("enter the id of the appointment whose appointment want to delete "))
    sure=input("\n****Are you sure to cancel the appointment if yess then press'Y'or'y'*** ")
    if sure==("y" or "Y"):
        stime="update appoinment set start_time='{}' where id ={}".format("Cancel",cancel)
        etime="update appoinment set end_time='{}' where id ={}".format("Cancel",cancel)
        cur.execute(stime)
        cur.execute(etime)
        mycon.commit()
        mycon.close()
        print("Record has been canceld")
    else:
        print("Record is not canceld")
        return


#For (admin then => change pass)

def changepass():
    while True:
        b=input("\nenter the old password ")
        file=open("admin.txt",'r')
        z=file.read()
        if z==b:
            file=open("admin.txt",'w')
            passwd=input("Enter new Password ")
            file.write(passwd)
            file.close()
            print("\nYOUR PASSWORD IS CHANGED SUCCESSFULLY\n")
            return
        else:
            print("\nYou Write Wrong Password Try Again")
        
 



#For doctor window
def doctor():
    print("\n\t***********************************************")
    print("\n\t************WELCOME TO CITY HOSPITAL***********")
    print("\n\t***********************************************")
    while True:
        print("\n\t\t-------Welcome to doctor's window-------")
        print("\n***doctor's Options***")
        q2=int(input("Press 1 to view hospital doctor's details\nPress 2 to view own details\nPress 3 to view whome I am appoint"))
        if q2==1:
            hosdoc()
        elif q2==2:
            owndet()
        elif q2==3:
            wappoint()
        else:
            print("wrong choice")

#view hospital doctor
def hosdoc():
    import mysql.connector
    mycon=mysql.connector.connect(host='localhost',user='root',passwd='piyush',database='hospital')
    cur=mycon.cursor()
    view="select name,gender,department,phone_no,address from doctor"
    cur.execute(view)
    row=cur.fetchall()
    for c in row:
        print(c)
    mycon.close()
        
def owndet():
    id=int(input("enter your personal id"))
    import mysql.connector
    mycon=mysql.connector.connect(host='localhost',user='root',passwd='piyush',database='hospital')
    cur=mycon.cursor()
    show="select * from doctor where id={}".format(id)
    cur.execute(show)
    row=cur.fetchall()
    print(row)
    mycon.close()

def wappoint():
    name=int(input("enter correct name"))
    import mysql.connector
    mycon=mysql.connector.connect(host='localhost',user='root',passwd='piyush',database='hospital')
    cur=mycon.cursor()
    show="select * from appoinment where doctor_name='{}'".format(name)
    cur.execute(show)
    

                     
    







#For patient window

def patient():
    print("\n\t***********************************************")
    print("\n\t************WELCOME TO CITY HOSPITAL***********")
    print("\n\t***********************************************")
    while True:
        print("\n\t\t-------Welcome to patient's window-------")
        print("\n***patient's Options***")
        q2=int(input("Press 1 to view hospital doctor's details\nPress 2 to view own details"))
        if q2==1:
            hosdoc()
        elif q2==2:
            ownpdet()
        else:
            print("wrong choice")

def ownpdet():
    id=int(input("enter your personal id"))
    import mysql.connector
    mycon=mysql.connector.connect(host='localhost',user='root',passwd='piyush',database='hospital')
    cur=mycon.cursor()
    show="select * from patient where id={}".format(id)
    cur.execute(show)
    row=cur.fetchall()
    print(row)
    mycon.close()





#START From here
print("\n\t***********************************************")
print("\n\t************WELCOME TO CITY HOSPITAL**********")
print("\n\t***********************************************")

print("Press 1 for Admin Window\nPress 2 for Doctor Window\nPress 3 for Patient Window")
ch=int(input("enter the choice:-"))
if ch==1:
    admin()
elif ch==2:
    doctor()
elif ch==3:
    patient()
else:
    print("WRONG CHOICE")
        
        
    

