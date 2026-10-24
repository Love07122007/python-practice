#returns its square
'''def square(num):
    return num*num

print(square(4))

#returns true if no is even else false
def even(num):
    if num % 2 == 0:
        return True
    else:
        return False
print(even(4))

#largest of three numbers
def largest(a, b, c):
    if a > b and a > c:
        return a
    elif b > c:
        return b
    else:
        return c
print(largest(1, 2, 3))

#Write a function calculate(a, b) that returns the sum, difference, product, and
#division of two numbers.
def calculate(a, b):
    sum = a + b
    difference = a - b
    product = a * b
    division = a / b if b != 0 else "Error: Division by zero is not allowed."
    return sum, difference, product, division

print(calculate(10, 5))

#Write a function student_result(marks) that accepts a list of marks and returns:

#Total marks, Average marks, Highest marks, Lowest marks
def student_result(marks):
    total = sum(marks)
    average = total / len(marks) 
    highest = max(marks) 
    lowest = min(marks) 
    return total, average, highest, lowest

print(student_result([85, 92, 78, 96, 88]))#ye meri choice hai input lena hai ya nhi

#Write a function count_vowels(text) that accepts a string and returns the number of
#vowels in it.
def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count

print(count_vowels("Hello, World!"))

#Write a function reverse_number(n) that returns the reverse of a number.
def reverse_number(n):
    reversed_num = 0
    while n > 0:
        digit = n % 10
        reversed_num = reversed_num * 10 + digit
        n //= 10
    return reversed_num

print(reverse_number(12345))#input lena hai ya nhi ye meri choice hai

#11.Write a function check_prime(n) that returns whether a number is prime or not.
def check_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

print(check_prime(7))

#13.Write a function sum_of_digits(n) that returns the sum of digits of a number.
def sum_of_digits(n):
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total

print(sum_of_digits(12345))

#14.Write a function count_numbers(numbers) that accepts a list and returns the number
#of: Positive numbers, Negative numbers, Zeros
def count_numbers(numbers):
    positive_count = 0
    negative_count = 0
    zero_count = 0

    for num in numbers:
        if num > 0:
            positive_count += 1
        elif num < 0:
            negative_count += 1
        else:
            zero_count += 1

    return positive_count, negative_count, zero_count

print(count_numbers([1, 2, 3, -4, -5, 0]))

#15.Write a function get_grade(marks) that returns the grade according to:

#90–100 → A, 80–89 → B, 70–79 → C, 60–69 → D, Below 60 → F
def get_grade(marks):
    if marks >= 90:
        return 'A'
    elif marks >= 80:
        return 'B'
    elif marks >= 70:
        return 'C'
    elif marks >= 60:
        return 'D'
    else:
        return 'F'

print(get_grade(85))

#17. Simple Calculator: Organise a calculator program using separate functions: add(),

#subtract(), multiply(), divide()
#The main program should ask the user for two numbers and an operation.

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero is not allowed."

print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = input("Enter choice (1/2/3/4): ")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == '1':
    print("Result:", add(num1, num2))
elif choice == '2':
    print("Result:", subtract(num1, num2))
elif choice == '3':
    print("Result:", multiply(num1, num2))
elif choice == '4':
    print("Result:", divide(num1, num2))
else:
    print("Invalid input")

#Shopping Bill: Create separate functions: input_items(), calculate_total(),

#calculate_discount(), generate_bill()
#The program should accept item prices and quantities and finally display the bill.

def input_items():
    items = {}
    while True:
        item = input("Enter item name (or 'done' to finish): ")
        if item == 'done':
            break
        price = float(input("Enter item price: "))
        items[item] = price
    return items

def calculate_total(items):
    total = sum(items.values())
    return total

def calculate_discount(total):
    if total > 100:
        discount = total * 0.1  # 10% discount for bills over $100
    else:
        discount = 0
    return discount

def generate_bill(items):
    total = calculate_total(items)
    discount = calculate_discount(total)
    final_total = total - discount

    print("\n--- Bill ---")
    for item, price in items.items():
        print(f"{item}: ${price:.2f}")
    print(f"Total: ${total:.2f}")
    print(f"Discount: ${discount:.2f}")
    print(f"Final Total: ${final_total:.2f}")

items = input_items()
generate_bill(items)'''