#create a list of five cities and print in reverse order using slicing
'''cities=["delhi","alberquerque","new york","london","los angles"]
print(cities[::-1])
print(cities[4:0:-1])
print(cities[-1:-6:-1])'''
#indexing left to right hi possible hai bss
#reverse indexing right to left bhi possible hai

#create two lists and combine them
'''list_1=[1,2,3,4,5]
list_2=[1,6,7,8,9]
list_1.extend(list_2)
print(list_1)'''
#or we can use the concatinate

#create a list and display it three times
'''list=[1,2,3,4]
print([list]*3)'''#this is repetition operator

#create a list of five fruits and and add one more and insert your favourite colour at second position
'''list = ["apple","mango","banana","orange","cherry"]
list.append("guava")
list.insert(1,"black")#insert me hmm index ke acc krr skte hai
print(list)'''

#last element remove krne ke liye pop ka use kro or agr index include kroge
#to ushi index ka element remove hoga 
#or combine krne ke liye extend ka use krr skte hai

#wap to remove third element using 'del' now remove third and then remove all
list=[1,2,3,4]
del(list[2])
print(list)
list.clear()
print(list)
#delete function ka use hmm aese krte hai 

#wap to sort in asec and dsec
'''list=[1,2,3,4]
list.sort()
print(list)
list.sort(reverse=True)
print(list)'''

'''list=[1,2,3,4,5]
list2 = list.copy()
print(list)
print(list2)'''
#copy functin se shallow copy bnti hai

#count kro duplicates ko
'''list=[1,1,1,2,2,2,3,3,4,4,5,5]
print(list.count(1))
print(list.count(2))
print(list.count(3))
print(list.count(4))
print(list.count(5))'''
# count return krta hai isliye usko print kra skte hai

'''list=[1,2,3,4]
print(list.index(3))'''

#create a nested list representing 3 by 3 matrix 
'''matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix)'''

#list comprehension above question 
'''matrix = [[0 for j in range(3)] for i in range(3)]

print(matrix)'''

#other example of list comprehension
'''matrix = [[j for j in range(3)] for i in range(3)]

print(matrix)'''
#simple example of list comprehension
'''numbers = [x for x in range(5)]
print(numbers)'''

#with condition
'''numbers = [x for x in range(10) if x % 2 == 0]
print(numbers)'''


#enumerate function ka use krke index ke sath print krna
names = ["Ram", "Shyam", "Mohan"]

for index, name in enumerate(names):
    print(index, name)

#without enum sirf iske elements print ho skte hai 
#printing a 3 by 3 matrix from 1to 9 by list and list comprehension
matrix =[[i*3+j+1 for j in range(3)]for i in range(3)]
print(matrix)