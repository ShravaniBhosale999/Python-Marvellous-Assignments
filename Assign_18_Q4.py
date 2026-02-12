# Program to find frequency of a number in the list

def Frequency(arr, num):
    return arr.count(num)

n = int(input("Enter number of elements: "))
arr = []

for i in range(n):
    arr.append(int(input()))

search = int(input("Enter element to search: "))
print("Output:", Frequency(arr, search))
