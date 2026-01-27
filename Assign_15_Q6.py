# Program to accept a list of numbers and return sum of even numbers using reduce()
from functools import reduce

nums = [1, 2, 3, 4, 5, 6]
result = reduce(lambda a, b: a + b if b % 2 == 0 else a, nums, 0)
print(result)
