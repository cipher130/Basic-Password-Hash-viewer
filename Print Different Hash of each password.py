#Custom hash comparison of different hashes depending on hash type E.G. SHA256, MD5, SHA3-256

import hashlib
import getpass

print("""
          Hello, this is a program where you can view the hashes of 3 different hash types: SHA256, MD5, SHA3-256.
          you enter your password and we'll output the 3 different hashes in 3 different lines for your password.
          """)
password = input("Enter the password you'd like to view the hashes of: ")
hashed_password = hashlib.sha256(password.encode()).hexdigest()
print("This is the hash in SHA-256\n", hashed_password)
hashed_password2 = hashlib.md5(password.encode()).hexdigest()
print("\nThis is the hash in MD5\n", hashed_password2)
hashed_password3 = hashlib.sha3_256(password.encode()).hexdigest()
print("\nThis is the hash in SHA3-256\n", hashed_password3)
