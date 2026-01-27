# Program to accept a list of numbers and return largest even number using reduce()
from functools import reduce

nums = [10, 15, 22, 8, 7]
result = reduce(lambda a, b: b if b % 2 == 0 and b > a else a, nums, 0)
print(result)
