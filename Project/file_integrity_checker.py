import hashlib
filename = input("Filename: ")

sha = hashlib.sha256()
with open(filename, "rb")as f:
    while True:
        chunk = f.read(4096)
        if not chunk:
            break
        sha.update(chunk)

print("SHA256: ")
print(sha.hexdigest())