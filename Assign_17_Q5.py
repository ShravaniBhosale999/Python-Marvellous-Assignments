#Program to check whether a number is prime or not

num = int(input("Enter number: "))

if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print("It is not Prime Number")
            break
    else:
        print("It is Prime Number")
else:
    print("It is not Prime Number")
