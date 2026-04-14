# Write a Python program to rename all files in a specified directory by changing their file extension. The program should take the directory path, the old file extension, and the new file extension as input from the user and rename all matching files accordingly.

import os
import sys

def rename_files(directory, old_ext, new_ext):
    for file in os.listdir(directory):
        if file.endswith(old_ext):
            new_name = file.replace(old_ext, new_ext)
            os.rename(os.path.join(directory, file),
                      os.path.join(directory, new_name))

if __name__ == "__main__":
    rename_files(sys.argv[1], sys.argv[2], sys.argv[3])