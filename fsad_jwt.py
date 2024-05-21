import secrets, jwt,time
 
secret = secrets.token_hex(32)
print("Generated secret: ",secret)

payload = {
    "username": "2023sl93034",
     "name"  : "jitendra kumar shah",
     "userID": 1309,
    "subject": "FSAD",
    "custom_claim": "demo",
    "exp": int(time.time()) + 60 * 60  # Add expiration time (1 hour)
}


print("original string: ", payload)
print("----------------------------------------------------------------")

token = jwt.encode(payload, secret, algorithm='HS256')
 
print("Generated JWT token:", token)
print("-------------------------------------------")
received_token = token

try:
    decoded = jwt.decode(received_token, secret, algorithms=['HS256'])
    print("\nDecoded payload:", decoded)
except jwt.exceptions.PyJWTError as e:
    print("Invalid JWT:", e)

 