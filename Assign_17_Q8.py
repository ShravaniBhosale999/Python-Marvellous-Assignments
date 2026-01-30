#program to print the pattern

n = int(input("Enter number: "))

for i in range(1, n + 1):        # rows
    for j in range(1, i + 1):    # numbers
        print(j, end=" ")
    print()

