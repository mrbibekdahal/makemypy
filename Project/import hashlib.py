import hashlib

name = input("Name: ")

h = hashlib.sha256(name.encode())

print(h.hexdigest())