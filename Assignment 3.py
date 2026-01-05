# Assignment 3

# Q1. User-defined function to multiply two numbers
def multiply(a, b):
    return a * b


# Q3. Scope example
def fun():
    x = 10
    print(x)

fun()
# print(x)  # Uncommenting this will cause NameError


# Q4. Function that prints message but returns nothing
def show():
    print("Hello World")


# Q6. Display datatype, memory address, size
import sys
x = input("Enter value: ")
print(type(x))
print(id(x))
print(sys.getsizeof(x))


# Q7. Dynamic typing
a = 5
print(type(a))

a = 5.5
print(type(a))

a = "Python"
print(type(a))
