#tuple
'''tup=(1,1,2,2,23,8)
count=tup.count(2)#jo function value return krega usko print kra skte
print(count)
print(tup.index(2))#ya ek or variable me hold krr skte hai

#concatinate 
tup1=(1,2,3,4)
tup2=(5,6,7,8)
print(tup1+tup2)
print((3)*(tup1+tup2)) #repetition 3 times 

#reverse a tuple using slicing find max min sum and average 
tup3=(1,2,3,4,5,6,7)
print(tup3[-1:-8:-1])#reversing a tuple using indexing 
#sum=tup3.sum() this is not possible in tuple bcz sum is python in built
#function not tuple in built fun so tuple ke sath dot nhi le skte
sum =sum(tup3)
print("sum",sum)#sum
print("max",max(tup3))#maximum
average = sum/len(tup3)
print(average)
print("min",min(tup3))

tup4=([1,2,3,4],"raju","ajay",8,9,10)
print(tup4[0][3])#accessing the elements of a tuple inside a list
#same goes for the list

#packing unpacking and extended unpacking
tup=("love",21,"cse","python")
print(tup) #all together packed in one tuple so tup packing

name,age,branch,subject=tup #unpacking
print(name)
print(age)
print(branch)
print(subject)

#now extended unpacking
name, *other,last=tup # * operator ke sath baaki ka pura hojata hai
print(other)#ye list ki tarah hi print hoga kyuki python ka feature hai ye

#swap using tuple unpacking
swap=(1,2)
a,b=swap
temp=a
a=b
b=temp
print(a,b)

#store students records as tuple inside a list and display names with marks
students = [
    ("Rahul", 85),
    ("Aman", 78),
    ("Priya", 92),
    ("Neha", 88)
]

for name, marks in students:
    print("Name:", name, "Marks:", marks)'''

#generate squares of numbers from 1to10
squares=(x*x for x in range(1,11))
print(squares)