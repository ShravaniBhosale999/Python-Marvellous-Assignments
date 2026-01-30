#Program to perform arithmetic operations using a module named Arithmatic
import Arithmatic

a= int(input("Enter first number: "))
b= int(input("Enter second number: "))

print("Addition is", Arithmatic.add(a,b))
print("Subtraction is", Arithmatic.subtract(a,b))
print("Multiplication is", Arithmatic.multiply(a,b))
print("Division is", Arithmatic.divide(a,b))