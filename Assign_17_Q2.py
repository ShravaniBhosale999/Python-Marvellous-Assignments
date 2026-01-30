#Program to print a square pattern of stars

n = int(input("Enter number: "))

for i in range(n):
    print("* " * n)


#OR

for i in range(5):
    for j in range(5):
        print("*", end=" ")
    print()
