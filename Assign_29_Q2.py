fname = input("Enter the file name: ")

with open(fname, 'r') as f:
    data = f.read()
    print(data)
    