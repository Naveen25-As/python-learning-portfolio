# Duplicate File Finder.

import os
import hashlib


def get_hash(file_path):
    hasher = hashlib.md5()

    with open(file_path, "rb") as file:
        while chunk := file.read(4096):
            hasher.update(chunk)

    return hasher.hexdigest()


folder = input("Enter folder path: ")

hashes = {}
duplicates = []

for root, dirs, files in os.walk(folder):

    for filename in files:

        path = os.path.join(root, filename)

        try:
            file_hash = get_hash(path)

            if file_hash in hashes:
                duplicates.append((path, hashes[file_hash]))
            else:
                hashes[file_hash] = path

        except PermissionError:
            continue


print("\n===== DUPLICATES =====")

if not duplicates:
    print("No duplicate files found.")
else:
    for duplicate, original in duplicates:
        print("\nDuplicate:", duplicate)
        print("Original:", original)