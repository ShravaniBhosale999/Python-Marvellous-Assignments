## Program to find maximum element from the list

arr = []

def MaxElement(arr):
    return max(arr)

n = int(input("Enter number of elements: "))

for i in range(n):
    arr.append(int(input()))

print("Output:", MaxElement(arr))