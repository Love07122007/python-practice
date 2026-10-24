'''a=int(input("the first number is:" ))
b=int(input("the second number is: "))
print("are they equal",a==b)
print("are they not equal",a!=b)
print("is a greater than b",a>b)
print("is a less than or equal to b",a<=b)'''
 #input subject two marks 
sub1 = int(input("Enter marks for subject one: "))
sub2 = int(input("Enter marks for subject two: "))
if(sub1>=35 and sub2>=35):
    print("pass")   
else:
    print("fail")
if(sub1>=90 or sub2>=90):
    print("eligible for scholarship")
else:
    print("not eligible for scholarship")
#ek variable bnana padega failed
failed = sub1<35 or sub2<35
if not failed:
    print("student has not failed in any subject")
else:
    print("student has failed in at least one subject")
# not operator ka use krna hai isliye do if else toh lagenge hi atleast
