key = 45
text = input("message: ")
encrypted = ""
for ch in text:
    encrypted += chr(ord(ch) ^ key)

print("Encrypted: ",encrypted)

decrypted = ""
for ch in encrypted:
    decrypted += chr(ord(ch) ^ key)

print("Decrypted: ",decrypted)
