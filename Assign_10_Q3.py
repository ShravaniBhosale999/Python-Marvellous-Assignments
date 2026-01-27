#program to find factorial of a numbe

def factorial(n):
    if n == 1:
        return 1 
    else:
        return n*factorial(n-1)
No1=(int(input("Enter a positive integer to find its factorial: ")))
result = factorial(No1)
print("Factorial is:",result)