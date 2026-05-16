# -------- 1. PRINT STATEMENT --------
print("Hello, Welcome to Python Basics!\n")


# -------- 2. VARIABLES --------
name = "Praveen"
age = 20
height = 5.8
is_student = True

print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Student:", is_student)
print()


# -------- 3. DATA TYPES --------
integer_num = 10
float_num = 10.5
string_text = "Python"
boolean_value = False

print(type(integer_num))
print(type(float_num))
print(type(string_text))
print(type(boolean_value))
print()


# -------- 4. USER INPUT --------
user_name = input("Enter your name: ")
print("Hello", user_name)
print()


# -------- 5. TYPE CASTING --------
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

sum_result = num1 + num2
print("Sum:", sum_result)
print()


# -------- 6. OPERATORS --------
a = 10
b = 3

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Modulus:", a % b)
print()


# -------- 7. CONDITIONAL STATEMENTS --------
marks = int(input("Enter your marks: "))

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")
print()


# -------- 8. LOOPS --------
print("For Loop:")
for i in range(1, 6):
    print(i)

print("\nWhile Loop:")
count = 1
while count <= 5:
    print(count)
    count += 1
print()


# -------- 9. LIST --------
fruits = ["Apple", "Banana", "Orange"]

print("List:", fruits)
print("First fruit:", fruits[0])

fruits.append("Mango")
print("After append:", fruits)
print()


# -------- 10. TUPLE --------
colors = ("Red", "Blue", "Green")
print("Tuple:", colors)
print()


# -------- 11. SET --------
numbers = {1, 2, 3, 3, 4}
print("Set:", numbers)
print()


# -------- 12. DICTIONARY --------
student = {
    "name": "Arfin",
    "age": 20,
    "course": "Python"
}

print("Dictionary:", student)
print("Student name:", student["name"])
print()


# -------- 13. FUNCTIONS --------
def greet(name):
    return f"Hello {name}"

message = greet("Arfin")
print(message)
print()


# -------- END --------
print("Python Basics Completed Successfully!")