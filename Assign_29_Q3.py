import sys

src = sys.argv[1]
with open(src, "r") as f1, open("Demo.txt", "w") as f2:
    f2.write(f1.read())
    print("Copied successfully")