# Program to accept a list of numbers and return smallest number using reduce()
from functools import reduce

nums = [25, 10, 40, 5, 15]
result = reduce(lambda a, b: a if a < b else b, nums)
print(result)
