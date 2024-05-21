from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
 
# Generate private key
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)
 
# Save the private key to a file
with open("private_key.pem", "wb") as private_file:
    private_file.write(
        private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption()
        )
    )
 
# Generate public key
public_key = private_key.public_key()
 
# Save the public key to a file
with open("public_key.pem", "wb") as public_file:
    public_file.write(
        public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )
    )

import jwt
import time
from cryptography.hazmat.primitives import serialization
 
# Load the private key
with open("private_key.pem", "rb") as private_file:
    private_key = private_file.read()
 
# Payload
payload = {
    "username": "2023sl93034",
     "name"  : "jitendra kumar shah",
     "userID": 1309,
     "msg":"using key pair method",
    "subject": "FSAD",
    "custom_claim": "demo",
    "exp": int(time.time()) + 60 * 60  # Add expiration time (1 hour)
}

 
# Generate JWT
token = jwt.encode(payload, private_key, algorithm='RS256')
 
print(token)