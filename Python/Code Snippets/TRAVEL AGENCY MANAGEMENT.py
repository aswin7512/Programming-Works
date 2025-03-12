import mysql.connector as sql
import sys
import os
p=input("ENTER PASSWORD: ")
os.system("clear")
conn=sql.connect(host='localhost',user='u0_a208',password=p)
c1=conn.cursor()
if conn.is_connected():
    c1.execute("SHOW DATABASES LIKE 'travel_booking';")
    row=c1.fetchone()
    if row==[] or row== None:
        c1.execute("create database travel_booking;")
        print("database created successfully")
        conn.commit()
        c1.execute('use travel_booking;')
        c1.execute('create table accounts(Phone_number bigint(13) primary key,name varchar(30),password  bigint(10));')
        conn.commit()

        c1.execute('create table customer_bookings(Phone_number bigint(13) ,FOREIGN KEY(Phone_number) REFERENCES accounts(Phone_number),Your_location varchar(30),Your_destination varchar(30),time varchar(30),Driver varchar(60),Urgency  varchar(30),date_booked varchar(90));')
        conn.commit()
    c1.execute('use travel_booking;')
    conn.autocommit==True

    from time import gmtime, strftime
    n=strftime("%a, %d %b %Y", gmtime())
    n=str(n)
    today=n[5:]
    print('                 ','___TRAVEL DAILY welcomes U!!!!!!___')
    print()
    print('                                   ',n)
    print()
    print('Press 1 to Login') 
    print('Press 2 Create account')
    print("press 3 delete account")
    print('Press 4 to Exit')
    print()
    choice=int (input('Enter your choice='))
    if choice ==1:
                    print()
                    a=int(input('Enter your phone number='))
                    #Name of the person
                    u=("select  name from accounts where phone_number = {};".format(a))
                    c1.execute(u)
                    #Wrong phone number[account doesn't exist]
                    datan=c1.fetchall()
                    s=c1.rowcount
                    s=abs(s)   
                    if s!= 1:
                        print()
                        print("********ACCOUNT DOESN'T EXIST*********")
                        print()
                        create=int(input("Press 32 to create account {{or}} Press 0 to exit="))
                        if create==32:
                            phone_number=int(input('Phone Number='))
                            name=input('Name=')
                            password =input( 'password[10]=')
                            c1.execute("insert into accounts(Phone_number,password,name )values(" + str(phone_number) +",'" +password  + "',' "+name+" ')")
                            conn.commit()
                            print('Account sucessfully Created')
                            sys.exit()
                        else:
                            sys.exit()
                        
                
                    datan=datan[0]
                    datan=list(datan)
                    datan= datan[0]
                    datan= str(datan)
                    y="select password from accounts where phone_number ={}".format(a)
                    c1.execute(y)
                    data=c1.fetchall()
                    data=data[0]
                    data=list(data)
                    data=data[0]

                    b=int(input('Enter your password='))
                    if b!=data:
                        print()
                        print("********INVALID PASSWORD*********")
                        conn.commit()        
                    else:
                        print()
                        print("LOGGED  IN !!!!!")
                        print()
                        print("HI",datan,"!!")
                        print()
                        print("What can I do for you?")
                        print()
                        print('12.Book for a board')
                        print('13.Bill verification')
                        print('14.My travel log')
                        print('0.Exit')
                        print()
                        choice1=int(input('Enter Your Choice='))
                        if choice1==0:
                            print()
                            print("Thank you , Visit again !!")
                            sys.exit()
                
                        elif choice1==12:
                            your_location=input('Your_location=')
                            your_destination=input('Your_destination=')
                            time=input('time to start board=')
                            driver=input("driver gender preferences=")
                            urgency=input('urgency(yes/no)=')
                            c1.execute("insert into customer_bookings values(" + str(a) +",' " +  your_location + " ' ,'  "+your_destination+ " ' ,' "+time+ " ' ,' "+driver+" ' ,' "+urgency+" ',' "+today+" ' )")
                            conn.commit()
                            print()
                            print('***********AT YOUR SERVICE AT',time,"***********")
                            sys.exit()
                       
                        
                        elif choice1==13:
                            Dist=int(input('distance travelled [km]='))
                            bill=Dist*5
                            print('your payment =Rs.',bill)
                        elif choice1==14:                
                            c1.execute("select  your_destination,date_booked from customer_bookings where phone_number like '"+str(a)+"';")
                            data=c1.fetchall()
                            for row in data:
                                   print(row[0],'-  {',row[1],'}')
                            conn.commit()
                            sys.exit()
                        else:
                                print()
                                print()
                                print("*******INVALID CHOICE*******")
                        sys.exit()
    elif choice==2:
        phone_number=int(input('Phone Number='))
        name=input('Name=')
        password =input( 'password[10]=')
        c1.execute("insert into accounts(Phone_number,password,name )values(" + str(phone_number) +",'" +password  + "',' "+name+" ')")
        conn.commit()
        print('Account sucessfully Created')
        sys.exit()

    elif choice==3:
        phone_number=int(input("enter your phone_number="))
        q1="delete from customer_bookings where phone_number ="+str(phone_number)+";"
        q2="delete from accounts where phone_number ="+str(phone_number)+";"
        c1.execute(q1)
        c1.execute(q2)
        conn.commit()
        print()
        print("*************SUCCESSFULLY ACCOUNT DELETED*************")
        sys.exit()
    
    elif choice==4:
        sys.exit()
    else:
        print()
        print()
        print("*******INVALID CHOICE*******")
conn.close()