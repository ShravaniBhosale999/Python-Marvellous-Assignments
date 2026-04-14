import sys

f1 = open(sys.argv[1], "r").read()
f2 = open(sys.argv[2], "r").read()
if f1 == f2:
    print("Files are same")
else:
    print("Files are different")

    