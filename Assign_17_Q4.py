#Program to find the sum of all factors of a number entered by the user
num = int(input("Enter number: "))
sum = 0

for i in range(1, num):
    if num % i == 0:
        sum += i

print("Output:", sum)




