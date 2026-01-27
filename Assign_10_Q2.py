def sum_natural_numbers(n):
    if n < 1:
        return 0
    else:
        return n + sum_natural_numbers(n - 1)
No1 = int(input("Enter a positive integer to find the sum of natural numbers up to that number: "))
result = sum_natural_numbers(No1)
print("The sum of natural numbers up to", No1, "is", result)
