#program to count the number of digits in a number

num = int(input("Enter number: "))
count = 0

while num > 0:
    count += 1
    num //= 10

print("Output:", count)
