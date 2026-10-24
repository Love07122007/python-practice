# Dictionary containing person details
'''person = {
    "name": "Rahul",
    "age": 25,
    "salary": 30000
}
# Display salary before update
print("Salary before update:", person["salary"])
# Update the salary
person["salary"] = 40000
# Display salary after update
print("Salary after update:", person["salary"])'''

#remove specific and last inserted item from dictionary
# Create a dictionary
'''person = {
    "name": "Rahul",
    "age": 25,
    "salary": 30000,
    "city": "Delhi"
}

# Remove a specific key
person.pop("age")

print("After removing age:", person)

# Remove the last inserted item
person.popitem()

print("After removing last item:", person)'''

'''# Create a dictionary
student = {
    "name": "Rahul",
    "age": 20,
    "marks": 85
}

# Print all keys
print("Keys:")
for key in student.keys():
    print(key)

# Print all values
print("\nValues:")
for value in student.values():
    print(value)

# Print all key-value pairs
print("\nKey-Value Pairs:")
for key, value in student.items():
    print(key, ":", value)'''

# Create a dictionary
'''student = {
    "name": "Rahul",
    "age": 20,
    "marks": 85
}

# Take key from user
key = input("Enter the key: ")

# Check whether the key exists
if key in student:
    print("Key exists in the dictionary")
else:
    print("Key does not exist in the dictionary")'''

#wap to calculate the total no. of key value pairs in a dictionary
# Create a dictionary
'''student = {
    "name": "Rahul",
    "age": 20,
    "marks": 85
}

# Calculate the total number of key-value pairs
total_pairs = len(student)

print("Total number of key-value pairs:", total_pairs)
#wap in py to create a dictionary from two given lists
# Create two lists
keys = ["name", "age", "marks"]
values = ["Rahul", 20, 85]

# Create a dictionary
result_dict = dict(zip(keys, values))

print(result_dict)'''

#create a nested dict with thw data of three students 
# Create a nested dictionary with data of three students
students = {
    "student1": {
        "name": "Rahul",
        "age": 20,
        "marks": 85
    },
    "student2": {
        "name": "Priya",
        "age": 22,
        "marks": 90
    },
    "student3": {
        "name": "Aman",
        "age": 19,
        "marks": 75
    }
}
print(students)
print(students["student1"])
print(students["student1"]["name"])
print(students["student1"]["age"])
print(students["student1"]["marks"])
