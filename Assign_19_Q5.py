# Program using filter, map and reduce

# Assignment 19 - Q5
# Filter prime numbers, multiply by 2, return maximum

from functools import reduce

# Function to check prime
def isPrime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

# Accept list from user
data = list(map(int, input("Enter numbers separated by space: ").split()))

# Filter prime numbers
filtered = list(filter(isPrime, data))
print("After filter (prime):", filtered)

# Multiply each by 2
mapped = list(map(lambda x: x * 2, filtered))
print("After map (x2):", mapped)

# Find maximum using reduce
if mapped:   # to avoid error if empty
    result = reduce(lambda a, b: a if a > b else b, mapped)
    print("Output of reduce (max):", result)
else:
    print("No prime numbers found.")