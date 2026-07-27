import hashlib
password = input("Password: ")
stored_hash = hashlib.sha256(password.encode()).hexdigest()
print("Stored: ",stored_hash)
check = input("Enter password again: ")
new_hash = hashlib.sha256(check.encode()).hexdigest()
if new_hash == stored_hash:
    print("Correct Password.")
else:
    print("Wrong Password.")
    