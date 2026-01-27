# Program to accept a list of numbers and return sum of all elements using reduce()
from functools import reduce

nums = [1, 2, 3, 4, 5]
result = reduce(lambda a, b: a + b, nums)
print(result)


