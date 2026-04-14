
# Write a Python program to delete duplicate files in a specified directory. The program should take the directory path as input from the user and remove any duplicate files based on their content, keeping only one copy of each file.
def delete_duplicates(directory):
    import os
    import hashlib

    hashes = {}

    for file in os.listdir(directory):
        path = os.path.join(directory, file)

        if os.path.isfile(path):
            h = hashlib.md5(open(path,'rb').read()).hexdigest()

            if h in hashes:
                os.remove(path)
                print("Deleted:", file)
            else:
                hashes[h] = file

delete_duplicates("Demo")