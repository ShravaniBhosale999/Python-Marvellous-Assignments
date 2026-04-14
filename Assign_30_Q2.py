fname = input("Enter file: ")
with open(fname, "r") as f:
    data = f.read()

    words = data.split()
    print("Words:", len(words))