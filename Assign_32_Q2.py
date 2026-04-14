# Write a Python program to find duplicate files in a given directory. The program should take the directory path as input from the user and print the names of all duplicate files.
import hashlib
import os

def get_hash(filepath):
    h = hashlib.md5()
    with open(filepath, 'rb') as f:
        h.update(f.read())
    return h.hexdigest()

def find_duplicates(directory):
    hashes = {}
    for file in os.listdir(directory):
        path = os.path.join(directory, file)
        if os.path.isfile(path):
            file_hash = get_hash(path)
            if file_hash in hashes:
                print("Duplicate:", file)
            else:
                hashes[file_hash] = file

find_duplicates("Demo")