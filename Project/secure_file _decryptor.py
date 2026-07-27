from cryptography.fernet import Fernet

key = input("Enter keY: ").encode()

cipher = Fernet(key)

with open("secret.enc", "rb") as f:
    encrypted = f.read()

decrypted = cipher.decrypt(encrypted)

with open("secret_decrypted.txt", "wb") as f:
    f.write(decrypted)

print("File restored.")