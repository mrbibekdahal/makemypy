
#file checksum
import hashlib

filename = input("Enter filename: ")
with open(filename, "rb") as f:
    data = f.read()

checksum = hashlib.md5(data).hexdigest()

print("MD5 Checksum: ")
print(checksum)

#verify checksum

import hashlib
filename = input("File: ")
excepted = input("Expected MD5: ")

with open(filename, "rb") as f:
    actual = hashlib.md5(f.read()).hexdigest()
    
if actual == excepted:
    print("File is valid.")

else:
    print("File has changed.")