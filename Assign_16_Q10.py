#Program to count the number of characters in a name provided by the user

name = input("Enter your name: ")
count = len(name)
print("Number of characters:", count)

#to ignore spaces while counting
name = input("Enter your name: ")
count = len(name.replace(" ", ""))
print("Number of characters:", count)
