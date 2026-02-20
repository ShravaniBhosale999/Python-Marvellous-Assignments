# Program using filter, map and reduce

from functools import reduce

data = [4, 34, 36, 76, 68, 24, 89, 23, 86, 90, 45, 70]

# Filter
filtered = list(filter(lambda x: x >= 70 and x <= 90, data))
print("After filter:", filtered)

# Map
mapped = list(map(lambda x: x + 10, filtered))
print("After map:", mapped)

# Reduce (product)
result = reduce(lambda a, b: a * b, mapped)
print("Output of reduce:", result)