import hashlib
def hash_password(password):
      # Create a new sha256 hash object
    hash_obj = hashlib.sha256()
  
      # Update the hash object with the bytes of the password
    hash_obj.update(password.encode('utf-8'))
  
      # Return the hexadecimal representation of the hash
    return hash_obj.hexdigest()

password = 'Hello'
hashed_password = hash_password(password)
print(hashed_password)
