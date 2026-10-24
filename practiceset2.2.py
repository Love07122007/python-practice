#wap to check whether a no. is negative zero or one
'''num=(input("enter your number:"))
if(num>0):
    print("num is positive")
elif(num<0):
    print("num is negative")
else:
    print("number is zero")'''

#even odd 
'''num2=int(input("enter the number"))
if(num2%2==0):
  print("num is even")
else:
  print("num is odd")'''

#largest among three numbers
'''num=int(input("enter first no."))
num2=int(input("enter second no."))
num3=int(input("enter third no."))
if(num>num2 and num>num3):
    print("num 1 is largest")
elif(num2>num and num2>num3):
    print("num 2 is largest")
else:
    print("num 3 is greatest")'''

#wap to check whether a given year is a leap year or not
'''year=int(input("enter the year"))
if(year%4==0 and year%100!=0 or year%400==0):
    print("year is leap year")
else:
    print("the given year is not a leap year")'''

#atm withdrawl
# Simple ATM Withdrawal Program
#do chiz dimag me rkho agr bc pin hi incorrect hai toh amount tak kaise 
#puchenge hum bc 
'''# Set the correct PIN and initial account balance
correct_pin = "1234"
balance = 5000

# Ask the user to enter their PIN
pin = input("Enter your PIN: ")

# Check if the entered PIN is correct
if pin == correct_pin:
    # If PIN is correct, ask for withdrawal amount
    amount = float(input("Enter amount to withdraw: "))
    
    # Check if the account has sufficient balance
    if amount <= balance:
        # Deduct the amount from balance
        balance -= amount
        print("Withdrawal successful!")
        print("Remaining balance:", balance)
    else:
        # If balance is not enough
        print("Insufficient balance. Try again.")
else:
    # If PIN is incorrect
    print("Incorrect PIN. Try again.")'''

#wap to check whether the student is eligible for scholarship or not
#criteria: student's percentage >= 85% and attendance <=75%

'''percentage=int(input("enter the percentage"))
attendance=int(input("enter the attendance"))
if(percentage>=85 and attendance<=75):
    print("eligible for scholarship")
else:
    print("not eligible for scholarship")'''

#username and password 
# Simple Login Validation Program

# Set the correct username and password
correct_username = "user123"
correct_password = "pass123"

# Ask the user to enter their username and password
username = input("Enter your username: ")
password = input("Enter your password: ")

# Check if both username and password are correct
if username == correct_username and password == correct_password:
    print("Login successful!")
else:
    print("Invalid username and password")



