

No1 = int(input("Enter a number: "))
sum=0
while No1>0:
    digit=No1%10
    sum = sum+digit
    No1=No1//10
print("The sum of digits in the given number is:",sum)

