#Program to find factorial of a number 

fact = int(input("Enter a number to find its factorial: "))

def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
result=factorial(fact)
print("Factorial of", fact, "is", result)