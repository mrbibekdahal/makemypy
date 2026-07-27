import hashlib

first_name = (input("First name: "))
love_name = (input("Love name: "))

name = "".join(sorted([first_name.lower(), love_name.lower()]))

hash_value = hashlib.sha256(name.encode()).hexdigest()

number = int(hash_value, 16)

percentage = number % 100 + 1

print(f"{percentage}%")



