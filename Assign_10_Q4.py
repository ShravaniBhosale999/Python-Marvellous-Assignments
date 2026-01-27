#Python program to print all even numbers from 1 to n

def even_nums(a):
    for i in range(1,a+1):
        if i%2==0:
            print (i)
a=int(input("Enter a number: "))
even_nums(a)