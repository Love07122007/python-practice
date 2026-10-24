user_category=input("Enter the user category student or faculty(staff)")
base_fees=0
discount=0
parking_fee=0
congestion_subcharge=0
electricity_bill=0
if(user_category=="student"):
    sub_category=input("ENTER THE USER SUB CATEGORY UG OR PG")
    if(sub_category=="UG"):
        base_fees = 500
    elif(sub_category=="PG"):
        base_fees = 350
    else:
        print("Invalid sub category for student")
        
else:
        sub_category=input("ENTER THE USER SUB CATEGORY RESIDENT OR GUEST")
        if(sub_category=="resident"):
            base_fees = 800
        elif(sub_category=="guest"):
            base_fees = 1200
        else:
            print("Invalid sub category for faculty(staff)")
cgpa=float(input("enter student cgpa"))          
if(user_category=="student"):
     if(cgpa>=8.5):
        discount=(base_fees*20)/100
     elif(cgpa>=7.5 and cgpa<8.49):
        discount=(base_fees*10)/100
     else:
        print("you will not get any discount on your base fees")

else:
    years_of_service=int(input("enter your years of service"))
    if(years_of_service>=10):
        discount=(base_fees*15)/100
    else:
        discount=0
vehicle_type=input("enter the vehicle type")
if(user_category=="student"):
    if(vehicle_type=="two wheeler"):
        parking_fee=200
    elif(vehicle_type=="four wheeler"):
        congestion_subcharge=150
        parking_fee=600 + congestion_subcharge
    else:
        parking_fee=0
else:
    if(vehicle_type=="two wheeler"):
        parking_fee=200
    elif(vehicle_type=="four wheeler"):
        parking_fee=600
    else:
        parking_fee=0
monthly_electricity_consumption=int(input("enter your monthly electricity consumption"))
if(user_category=="student" or user_category=="faculty(staff)"):
    if(monthly_electricity_consumption>=0 and monthly_electricity_consumption<=100):
        fixed_charge=50
        electricity_bill=(monthly_electricity_consumption*3) + fixed_charge
    elif(monthly_electricity_consumption>=101 and monthly_electricity_consumption<=300):
        fixed_charge=100
        electricity_bill=(monthly_electricity_consumption*5 )+ fixed_charge
    elif(monthly_electricity_consumption>=301 and monthly_electricity_consumption<=500):
        fixed_charge=150
        electricity_bill=(monthly_electricity_consumption*7.50 )+ fixed_charge
    else:
        fixed_charge=250
        electricity_bill=(monthly_electricity_consumption*10 )+ fixed_charge
    print("Base Access Pass Fees:", base_fees)
    print("Merit Discount:", discount)
    print("Parking Fee:", parking_fee)
    print("Electricity Bill:", electricity_bill)
    total_fees = base_fees - discount + parking_fee + electricity_bill
    print("TOTAL MONTHLY PAYABLE:", total_fees)
