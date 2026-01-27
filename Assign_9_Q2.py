#Q2. Write a Python program to find whether a given number (accept from the user) is gretaer than the two numbers (a, b) or not.
def chkgreater(a, b):
    if a > b:
        print(a, "is greater")
    elif b > a:
        print(b, "is greater")
    else:
        print("Both are equal")

NO1 = int(input("Enter first number: "))
NO2 = int(input("Enter second number: "))

chkgreater(NO1, NO2)
