# Write a Python program to search for files with a specific extension in a given directory and its subdirectories. The program should take the directory path and the file extension as input from the user and print the paths of all matching files.

import os
import sys

def search_files(directory, ext):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(ext):
                print(os.path.join(root, file))

if __name__ == "__main__":
    search_files(sys.argv[1], sys.argv[2])