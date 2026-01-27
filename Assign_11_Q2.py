No1=int(input("Enter a number: "))
count = 0
while No1>0:
    No1=No1//10
    count = count+1
print("The number of digits in the given number is:",count)