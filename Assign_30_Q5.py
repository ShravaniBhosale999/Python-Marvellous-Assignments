f1 = input("Enter source file: ")
f2 = input("Enter destination file: ")

with open(f1, "r") as src, open(f2, "w") as dest:
        dest.write(src.read())
print("File copied successfully")