'''sum=0
i=1
while(i<=10):
    if(i%2==0):
      sum+=i
    i+=1
print(sum)#sum of even numbers

#wap to read three numbers (a,b,c) and and chech how many no.s btw a and b
#are divisible by c
a=int(input("enter the first no."))
b=int(input("enter the second no."))
c=int(input("enter the third no."))
i=a
count=0
while(i<=b):
    if(i%c==0):
        count+=1
    i+=1
print(count)
#1--99, 2--98, 3--97, 4--96, 5--95, 6--94, 7--93, 8--92, 9--91, 10--90 

i=1
while(i<=99):
    print(i,"--",100-i)
    i+=1
#wap to read a number and print its binary equivalent using while loop
n=int(input("enter a number"))
binary=""
while(n>0):
    rem=n%2
    binary=str(rem)+binary
    n=n//2
print(binary)

#wap to read four numbers(representation the four octacts of an ip)
#and the next five ip adresseses

a = int(input("Enter first octet: "))
b = int(input("Enter second octet: "))
c = int(input("Enter third octet: "))
d = int(input("Enter fourth octet: "))

print("Original IP:", a, b, c, d, sep=".")

for i in range(5):#five ip adress or krne hai 
    d = d + 1

    if d > 255:
        d = 0
        c = c + 1

        if c > 255:
            c = 0
            b = b + 1

            if b > 255:
                b = 0
                a = a + 1

    print(a, b, c, d, sep=".")#next five ip addresses
#wap to print first 10 fibonacci numbers using while loop
a=0
b=1
i=1
while(i<=10):
    print(a,end=" ")
    c=a+b
    a=b
    b=c
    i+=1
#pattern right triangle
i=1
while(i<=5):
    j=1
    while(j<=i):
        print("*",end=" ")
        j+=1
    print()
    i+=1

    #wap to check whether a given no. is prive or not
num = int(input("Enter a number: "))

i = 2

if num < 2:
    print("Not a prime number")
else:
    while i < num:
        if num % i == 0:
            print("Not a prime number")
            break
        i = i + 1
    else:
        print("Prime number")

#wap to print num from  1 to 100 which is prime
num = 2

while num <= 100:
    i = 2

    while i < num:
        if num % i == 0:
            break
        i = i + 1

    if i == num:
        print(num)

    num = num + 1

#wap to find the sum of the digits of a given number
num = int(input("Enter a number: "))
sum = 0

while num > 0:
    rem = num % 10
    sum = sum + rem
    num = num // 10

print("Sum of digits:", sum)

#wap in python to read its reverse
num = int(input("Enter a number: "))
reverse = 0

while num > 0:
    rem = num % 10
    reverse = reverse * 10 + rem
    num = num // 10

print("Reverse:", reverse)
#wap to print all the perfect numbers between 1 to 100

for num in range(1, 101):
    sum = 0

    for i in range(1, num):
        if num % i == 0:
            sum = sum + i

    if sum == num:
        print(num)
#wap in python to findd the greatest common divisor of two numbers using while loop
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

while a != b:
    if a > b:
        a = a - b
    else:
        b = b - a

print("GCD:", a)
#for LCD find the least common multiple of two numbers using while loop
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

while a != b:
    if a > b:
        a = a - b
    else:
        b = b - a

print("LCD:", a * b)

#wap to print the permutations of given three variables using while loop
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

print("Permutations:")
print(a, b, c)
print(a, c, b)
print(b, a, c)
print(b, c, a)
print(c, a, b)
print(c, b, a)'''


