#program to print the pattern

num = int(input("Enter number: "))

for i in range(num):        #rows
    for j in range(1,num+1):        #numbers
        print(j, end=" ")
    print()

