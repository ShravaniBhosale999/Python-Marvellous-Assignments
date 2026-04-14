fname = input("Enter file: ")
word = input("Enter word: ")


with open(fname, "r") as f:
    data = f.read()

count = data.count(word)
print("Frequency:", count)

