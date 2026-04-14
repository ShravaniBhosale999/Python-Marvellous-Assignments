# Write a Python program to create a log file that records the names of duplicate files in a specified directory. The program should take the directory path as input from the user and generate a log file named "Log.txt" that lists the duplicate files along with their paths.
import os
import hashlib
import sys
import time

def get_hash(path):
    h = hashlib.md5()
    with open(path, 'rb') as f:
        h.update(f.read())
    return h.hexdigest()

def log_duplicates(directory):
    hashes = {}
    log_name = "Log.txt"

    with open(log_name, "w") as log:
        log.write("Duplicate Files Log\n")
        log.write("Time: " + time.ctime() + "\n\n")

        for file in os.listdir(directory):
            path = os.path.join(directory, file)

            if os.path.isfile(path):
                file_hash = get_hash(path)

                if file_hash in hashes:
                    log.write(f"Duplicate: {file}\n")
                else:
                    hashes[file_hash] = file

    print("Log file created:", log_name)


if __name__ == "__main__":
    log_duplicates(sys.argv[1])