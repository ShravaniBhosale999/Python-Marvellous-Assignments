#Program to check whether a number is prime or not

no = int(input("Enter a number: "))

if no <= 1:
    print(no, "is not a prime number")
else:
    for i in range(2, no):
        if no % i == 0:
            print(no, "is not a prime number")
            break
    else:
        print(no, "is a prime number")
