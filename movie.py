#wap to print three movies name in a list by taking input
movies = []
mov1 = input("enter movie name")
mov2 = input("enter second movie name")
mov3 = input("enter third movie name")
#movies = [mov1,mov2,mov3]
#print(movies)
# method 2 use builtin function append
movies.append(mov1)
movies.append(mov2)
movies.append(mov3)
print(movies)
#append kisi bhi list or tuple ke last me element add krtahai
#or isko short me krne ke liye hmm movies,append(input)le skte hai
#shyd without variable