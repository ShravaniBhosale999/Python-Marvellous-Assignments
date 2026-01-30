#program to calculate the sum of digits of a number

num = int(input("Enter number: "))
sum = 0

while num > 0:
    digit = num % 10
    sum += digit
    num //= 10

print("Output:", sum)
