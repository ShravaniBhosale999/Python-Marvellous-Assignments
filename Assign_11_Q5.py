#Python program to check whether a number is a palindrome or not

no = int(input("Enter a number: "))

original = no
reverse = 0

while no > 0:
    reverse = reverse * 10 + (no % 10)
    no = no // 10

if original == reverse:
    print("Palindrome")
else:
    print("Not Palindrome")
