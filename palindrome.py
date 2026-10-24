#shure se padhe toh bhi same or last se padhe toh bhi same
#copy method hme ek shallow copy bnake deta hai
# shallow means duplicate
#list is given [1,2,3,2,1]
list=[1,2,3,2,1]
copy_list=list.copy()
copy_list.reverse()
if(list==copy_list):
    print("the given list is palindrome ")
else:
    print("the list is not palindrome")    