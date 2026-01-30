#Program to print the pattern
num = int(input("Enter number: "))

for i in range(num, 0, -1):
    print("* " * i)


#OR
num = int(input("Enter number: "))

for i in range(num):
    for j in range(num - i):
        print("*", end=" ")
    print()
