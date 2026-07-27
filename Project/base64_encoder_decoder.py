import base64
text = input("Text: ")
encoded = base64.b64encode(text.encode())

print("Encoded: ")
print(encoded.decode())

decoded = base64.b64decode(encoded)

print("Decoded: ")
print(decoded.decode())
#base64 is an encoding scheme,not encryption
