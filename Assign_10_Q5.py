#Python program to print all odd numbers from 1 to n

def odd_nums(a):
    for i in range(1,a+1):
        if i%2==1:
            print (i)
a=int(input("Enter a number: "))
odd_nums(a)