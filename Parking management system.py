#connecting python and mysql
import mysql.connector as m
mycon=m.connect(host='localhost',user='root',passwd='1234',database='csc_project')
if mycon.is_connected():
    print("sucessfully connected")
#Parking Management System    
print('\t')
print(' ================================================================== ')
print('|        -----------PARKING MANAGEMENT SYSTEM-----------           |')
print(' ================================================================== ')

print(' $ Welcome To Parking Management system $')
print('\t')
print( '1.Park a vehicle','\n2.Checkout parked vehicle','\n3.Parking charges','\n4.Record of parked_vehicle')
print('\t')
req=input('Please select the action to be performed{1,2,3,4}:')
print('\t')
if req=='1':
    def Park():

        import mysql.connector as m
        mycon=m.connect(host='localhost',user='root',passwd='1234',database='csc_project')
        mycur=mycon.cursor()
        mycur.execute("create table if not exists Parking_info(Vehicle_owner varchar(30) not null,Vehicle_no varchar(20) primary key not null,vehicle_type varchar(10) not null,checkIN_time varchar(500) not null )")
        mycur.execute("create table if not exists Record(Vehicle_owner varchar(30) not null,Vehicle_no varchar(20)  not null,vehicle_type varchar(10) not null,checkIN_time varchar(500) not null )")
        mycon.commit()
        import time
        from datetime import datetime
        now = datetime.now()
        local_time=now.strftime("%d/%m/%Y %H:%M:%S")
        choice='y'
        while choice=='y':
            e = input("Vehicle Owner:")
            n = input("Vehicle Number(xxxx-xx-xxxx):")
            d = input("vehicle Type:")
            s = local_time
            query="insert into Parking_info values('{}','{}','{}','{}')".format(e,n,d,s)
            query_1="insert into Record values('{}','{}','{}','{}')".format(e,n,d,s)
            mycur.execute(query)
            mycur.execute(query_1)
            mycon.commit()
            print("\nVehicle checked-IN at:", local_time)
            choice = input("Press y if you want to make more Entry:")
            print("***********************************************************")
    Park()
elif req=='2':
    def checkout():
        import mysql.connector as m
        mycon=m.connect(host='localhost',user='root',passwd='1234',database='csc_project')
        mycur=mycon.cursor()
        remove=input("\nEnter vehicle no.:")
        v=input("vehicle type:")
        if v=="00":
            co1=int(input("duration of parking(day):"))
            cost1=int(co1)*int(30)
            print("kindly pay the parking charge of Rs.",cost1)
        elif v=="01":
            co2=int(input("duration of parking(day):"))
            cost2=int(co2)*int(50)
            print("kindly pay the parking charge of Rs.",cost2)
        elif v=="02":
            co3=int(input("duration of parking(day):"))
            cost3=int(co3)*int(100)
            print("kindly pay the parking charge of Rs.",cost3)
        import time
        from datetime import datetime
        now= datetime.now()
        current_time=now.strftime("%d/%m/%Y %H:%M:%S")
        query="delete from Parking_info where Vehicle_no ='{}'".format(remove,)
        mycur.execute(query)
        mycon.commit()
        print('\t')
        print('vehicle checked out at:',current_time)
        print('\tThank you for using our service')
        print("\n***********************************************************")
        choice=input("press y to checkout more vehicles:") 
        if choice=='y':
            checkout()
        else:
            pass
    print("***********************************************************")
    checkout()
elif req=='3':
    print('\t')
    print("\t  $ PARKING CHARGES $")
    print(" -------------------------------------------")
    print("|   Vehicle_type       |   Rate(per day)    |")
    print("|-------------------------------------------|")
    print("|   2_wheeler(00)      |     Rs.30          |")
    print("|   3_wheeler(01)      |     Rs.60          |")
    print("|   4_wheeler(02)      |     Rs.100         |")
    print(" ------------------------------------------- ")
    print('\t')
    print("***********************************************************")
elif req=='4':
    def record():
         import mysql.connector as m
         mycon=m.connect(host='localhost',user='root',passwd='1234',database='csc_project')
         mycur=mycon.cursor()
         mycur.execute("select * from parking_info")
         mydata=mycur.fetchall()
         nrec=mycur.rowcount
         print("Total no. of Vehicles Parked:",nrec)
         for row in mydata:
               print(row)
    print("***********************************************************")
    record()

   
        
        
    
    
    
    
    
        
    
    
    

    
    
 
    
    
    
        
        
