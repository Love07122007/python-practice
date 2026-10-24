
for i in range(1,6):
    for j in range(1,6-i):
        print("  ",end="")
    for k in range(1,i+1):
        print(i,end=" ")
    print()

#x ki power n using for loop
'''x=int(input("enter no. for power"))
n=int(input("enter power"))
for i in range(1,n+1):
    result=x**i
    print(f"{x}^{i}={result}")

#other method to calculate x ki power n using for loop
x = int(input("Enter the number: "))
n = int(input("Enter the power: "))

result = 1

for i in range(n):
    result = result * x

print("Answer =", result)

#wap in python to generate the calender of a month given the start days and no. of days in a month
start_day = int(input("Enter starting day (1=Monday, 7=Sunday): "))
days = int(input("Enter number of days in month: "))

print("Mon Tue Wed Thu Fri Sat Sun")

# Print spaces before the first day
for i in range(start_day - 1):
    print("    ", end="")

# Print the days
for day in range(1, days + 1):
    print(f"{day:3}", end=" ")#ye colon theek ke liye hai ki 3 space ka gap ho
    
    if (start_day + day - 1) % 7 == 0:
        print()
num = 0

for i in range(1, 5):
    for j in range(i):
        print(num, end="")
        num += 1
    print()'''

#pyramid pattern
for i in range(1, 7):

    for j in range(1, 7-i):
        print("  ", end="")

    for k in range(1, i+1):
        print(k, end=" ")

    for k in range(i-1, 0, -1):
        print(k, end=" ")

    print()