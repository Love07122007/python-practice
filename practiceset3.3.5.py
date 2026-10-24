#wap in py to add some elements 
'''s={1,2,3,4}
s.update([5,6,7])#add se ek baar me hi sare ho jayenge 
print(s)#add ka use bhi krr skte hai prr ek baar me ek hi element add hoga
#s.remove(3)#remove se ek hi element remove hoga agar vo nhi hua toh error
#print(s)
s.discard(5)#discard se agar element nahi hoga toh error nhi aayega
print(s)
s.pop()#pop se random element remove hoga
print(s)'''

#disjoint tab ek bhi element common na ho dono set me  tab disjoit hoga 
#intersection tab ek bhi element common ho dono set metab intersection hoga
'''a={1,2,3,4}
b={3,4,5,6}
print(a.isdisjoint(b))
list=[1,1,1,2,2,3,3,4,4,5,5]
print(set(list))#set me duplicate value nhi aayegi
science_club={"aman","riya","rahul","priya","ankit"}
coding_club={"rahul","riya","ankit","simran","rohit"}'''
import matplotlib.pyplot as plt
# Data

x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 30, 25]

# Create a line graph

plt.plot(x, y)

# Add title and labels

plt.title("My First Graph")
plt.xlabel("X Values")
plt.ylabel("Y Values")

# Display the graph

plt.show()

