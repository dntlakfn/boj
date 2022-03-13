import hashlib

str = "k"

result = hashlib.sha256(str.encode())
print(result.hexdigest())
