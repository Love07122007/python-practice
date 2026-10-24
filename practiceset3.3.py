#strings 
#basics len type etc
'''str=input("enter a string:")
print(str)
print(len(str))
print(type(str))

#slicing on string 
str="my self aerion brightflame"
print(str[0:5])
print(str[-1:-6:-1])
print(str[::2])
print(str[3:10])
reverse=str[::-1]
print(reverse)
#count the uppercase and lowercase 

string = input("Enter a string: ")

uppercase = 0
lowercase = 0
digits = 0
spaces = 0
special = 0

for char in string:
    if char.isupper():
        uppercase += 1
    elif char.islower():
        lowercase += 1
    elif char.isdigit():
        digits += 1
    elif char.isspace():
        spaces += 1
    else:
        special += 1

print("Uppercase letters:", uppercase)
print("Lowercase letters:", lowercase)
print("Digits:", digits)
print("Spaces:", spaces)
print("Special characters:", special)


#or sum operator ka bhi use krr skte hai
s = input("Enter a string: ")

uppercase = sum(c.isupper() for c in s)
lowercase = sum(c.islower() for c in s)
digits = sum(c.isdigit() for c in s)
spaces = sum(c.isspace() for c in s)
special = sum(not c.isalnum() and not c.isspace() for c in s)

print("Uppercase:", uppercase)
print("Lowercase:", lowercase)
print("Digits:", digits)
print("Spaces:", spaces)
print("Special characters:", special)

#palindrome 

string=input("enter the string:")
reverse=string[::-1]
if(string==reverse):
    print("the string is palindrome")
else:
    print("the string is not palindrome")

#wap tp replace every space with  a hyphen in a string
str= "love tevatia"
print(str.replace(" ","-"))

#wap to check that two strings are anagrams or not
str1=input("enter the first string:")
str2=input("enter the second string:")
if(sorted(str1)==sorted(str2)):
    print("the strings are anagrams")
else:
    print("the strings are not anagrams")'''
#ex of anagrams 
#listen and silent


#wap to find the frequency of each character in a string
# Take a string from the user
'''s = input("Enter a string: ")

# Check each character
for ch in s:
    # Count how many times the character occurs
    count = s.count(ch)

    # Print the character and its frequency
    print(ch, ":", count)'''
#wap in python to input a sentence and display every word in the new line
'''sentence = input("Enter a sentence: ")
sentence = sentence.split()  # Split the sentence into words
for word in sentence:
    print(word)  # Print each word on a new line'''

#wap in python to reverse the order of words in a sentence
# Take a sentence from the user
'''sentence = input("Enter a sentence: ")

# Split the sentence into words
words = sentence.split()

# Reverse the order of words
words.reverse()

# Join the words back into a sentence
result = " ".join(words)

# Display the result
print(result)'''
#wap to remove duplicate characters from a string
# Take a string from the user
s = input("Enter a string: ")

# Empty string to store the result
result = ""

# Check each character
for ch in s:
    # Add character only if it is not already present
    if ch not in result:
        result += ch

# Display the result
print("String after removing duplicates:", result)

#wap in python to find the longest word in a sentence
# Take a sentence from the user
'''sentence = input("Enter a sentence: ")

# Split the sentence into words
words = sentence.split()

# Find the longest word
longest_word = max(words, key=len)
#key=len ek argument hai jo len ke basis pe check krega wrna ye alphabetical order me check krega
# Display the longest word
print("Longest word:", longest_word)'''


