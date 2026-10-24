#wap to display user entered name followed by the goodafternoon
name = input("enter your name ")
print("good afternoon",name)

#wap to detect the double space in a string
str1 = "love  choudhary"
print(str1[0:8])
#or in operator se bhi check krr skte hai using if else
#isse pta chalega ki spaces bhi count honge 
#or special characters bhi count honge 

#wap to replace the double space from the 
#problem 3 into single space
str2 = "love  choudhary"
str2 = str2.replace("  "," ")
print(str2)
