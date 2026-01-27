#Python program to reverse a number

no = int(input("Enter a number: "))

reverse = 0
while no > 0:
    reverse = reverse * 10 + (no % 10)
    no = no // 10

print(reverse)
