"""import secrets
import string

alphabet = string.ascii_letters+string.digits+"!@#$%^&*"
password = "".join(secrets.choice(alphabet) for _ in range(24))

print(f"password:{password}")"""

import secrets

password = secrets.token_urlsafe(18)  # About 24 characters
print(password)
