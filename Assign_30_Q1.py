fname = input("Enter file: ")

with open(fname, "r") as f:
    print("Lines:", len(f.readlines()))