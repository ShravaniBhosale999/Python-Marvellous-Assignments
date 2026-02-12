# Program to add all prime numbers from the list

import Prime_Module
def ListPrime(arr):
    sum = 0
    for num in arr:
        if Prime_Module.ChkPrime(num):
            sum += num
    return sum

n = int(input("Enter number of elements: "))
arr = []

for i in range(n):
    arr.append(int(input()))

print("Output:", ListPrime(arr))
