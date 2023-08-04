# Import the AES module from the Cryptodome library
from Cryptodome.Cipher import AES

# Define the encryption key and nonce (used in AES encryption)
key = b"VMU6rnfypBZL9rq3"
nonce = b"VMU6rnfypBZL9Nce"

# Create an AES cipher object in EAX mode with the provided key and nonce
cipher = AES.new(key, AES.MODE_EAX, nonce)

# Encrypt the plaintext b"Hello World!" using the AES cipher
ciphertext = cipher.encrypt(b"Hello World!")

# Print the ciphertext (encrypted message)
print(ciphertext)

# Create a new AES cipher object in EAX mode with the same key and nonce
cipher = AES.new(key, AES.MODE_EAX, nonce)

# Decrypt the ciphertext using the AES cipher
plaintext = cipher.decrypt(ciphertext)

# Print the decrypted plaintext
print(plaintext)
