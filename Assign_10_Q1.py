#Program that accepts 1 no. and prints multiplication table of the no.

def multiplication_table(num):
    for i in range(1,11):
        print(num, "x", i, "=", num*i)
No1= int(input("Enter a number to print its multiplication table: "))
multiplication_table(No1)