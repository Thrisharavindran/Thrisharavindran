# Greeting Program
# Takes user name and age and prints a message

name = input("Enter your name: ")
age = int(input("Enter your age: "))

#using concatenation
print("Hello, " + name + "! You are " + str(age) + " years old.")
#using f-string
print(f"Hello, {name}! You are {age} years old.")
