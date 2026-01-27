#

factor = int(input("Enter a number to find its factorial: "))
print("Factors are", end=" ")
for i in range(1,factor+1):
    if factor%i==0:
        print (i)
 

