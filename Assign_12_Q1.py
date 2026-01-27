#Python program to check whether a character is a vowel or not

char =input("Enter a character to check if vowel: ")
if char in ('a','e','i','o','u','A','E','I','O','U'):
    print(char,"is a vowel")
else:
    print(char,"is not a vowel")