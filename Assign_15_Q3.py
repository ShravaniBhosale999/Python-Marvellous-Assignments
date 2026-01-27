# Program to accept a list of numbers and return maximum element using reduce()
from functools import reduce

nums = [10, 20, 5, 40, 15]
result = reduce(lambda a, b: a if a > b else b, nums)
print(result)
