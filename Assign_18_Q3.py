# Program to find minimum element from the list


arr = []

def minelement(arr):
    return min(arr)

n = int(input("Enter number of elements: "))

for i in range(n):
 arr.append(int(input("Enter element: ")))
print("Output:", minelement(arr))