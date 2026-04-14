fname = input("Enter file: ")

with open(fname, "r") as f:
    for line in f:
        print(line.strip())
    