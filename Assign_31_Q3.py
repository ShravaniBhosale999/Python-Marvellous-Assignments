import shutil
import sys
import os

def copy_directory(src, dest):
    if not os.path.exists(dest):
        os.mkdir(dest)

    for file in os.listdir(src):
        shutil.copy(os.path.join(src, file), dest)

if __name__ == "__main__":
    copy_directory(sys.argv[1], sys.argv[2])