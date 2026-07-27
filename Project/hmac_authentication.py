import hmac
import hashlib

secret = b"my_secret_key"
message = input("message: ").encode()

signature = hmac.new(secret,message,hashlib.sha256).hexdigest()

print("Signature: ")
print(signature)