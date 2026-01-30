#Program to add two numbers provided by the user

def AddNum(a,b):
    return a+b

if __name__ == "__main__":
    No1= int(input("Enter first number: "))
    No2= int(input("Enter second number: "))
    result = AddNum(No1,No2)
    print("Sum of the two numbers is:",result)