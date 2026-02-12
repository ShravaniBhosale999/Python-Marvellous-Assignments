# Program to add all elements from the list

def AddElements(arr):
    return sum(arr)

n = int(input("Enter number of elements: "))
arr = []

for i in range(n):
    arr.append(int(input()))

print("Output:", AddElements(arr))
