""" list
fruit = ["apple","banana","orange"]

 #print(fruit)
fruit.append("grape")
#print(fruit)
#print(fruit[1])
#print(len(fruit))
fruit.remove("apple")
print(fruit)

#tuple
colors = ("red", "green", "blue")
print(colors)
print(len(colors))
#colors[1] = "yellow" #tuple is immutable, cannot change values

#set
numbers ={1,2,3,2,3}
#print(numbers) set does not allow duplicates, so it will only print {1,2,3}
numbers.add(4)
#print(numbers)
#print(numbers[0]) set does not support indexing
numbers.remove(2)
print(len(numbers))

#dictionary
student = {"name": "Sara", "age": 15, "grade": "8th"}
#print(student)
print(student["name"])
student["age"] = 16
student["city"] = "New York"
del student["grade"]
print(len(student))
print(student)
"""
#if statement
praveen = int(input("Enter your amount:"))
if praveen >= 30:
    print("you can have a burger")
elif praveen >= 20:
    print("you can have a sandwich")
elif praveen >= 10:
    print("you can have a coke")
else:
    print("you don't have enough money for any food item")