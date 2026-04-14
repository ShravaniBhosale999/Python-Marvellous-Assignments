# Write a Python program to copy all files with a specific extension from one directory to another. The program should take the source directory, destination directory, and file extension as input from the user.

import os
import shutil
import sys

def copy_specific_files(src, dest, ext):
    try:
        # Create destination if not exists
        if not os.path.exists(dest):
            os.mkdir(dest)

        for root, dirs, files in os.walk(src):
            for file in files:
                if file.endswith(ext):
                    src_path = os.path.join(root, file)
                    dest_path = os.path.join(dest, file)

                    shutil.copy(src_path, dest_path)

        print("Files copied successfully")

    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    copy_specific_files(sys.argv[1], sys.argv[2], sys.argv[3])