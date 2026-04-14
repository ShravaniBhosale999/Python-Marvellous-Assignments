import os
import shutil
import sys

def copy_ext_files(src, dest, ext):
    if not os.path.exists(dest):
        os.mkdir(dest)

    for file in os.listdir(src):
        if file.endswith(ext):
            shutil.copy(os.path.join(src, file), dest)

if __name__ == "__main__":
    copy_ext_files(sys.argv[1], sys.argv[2], sys.argv[3])