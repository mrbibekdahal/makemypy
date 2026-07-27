from cryptography.fernet import Fernet

Key = input("key: ").encode()
encrypted = input("Encrypted Text: ").encode()

cipher = Fernet(Key)
decrypted = cipher.decrypt(encrypted)

print("Original: ")
print(decrypted.decode())
