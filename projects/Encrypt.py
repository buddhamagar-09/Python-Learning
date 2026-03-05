import random 
import string

chars = " " + string.punctuation + string.digits + string.ascii_lowercase + string.ascii_uppercase

chars = list(chars)
keys = chars.copy()
random.shuffle(keys)

# encrypt
text = input("Enter some text: ")
cipher_text = ""

for letter in text:
    index = chars.index(letter) 
    cipher_text += keys[index]

print(f"Original message: {text}")
print(f"Encrypted message: {cipher_text}")

# encrypt
cipher_text = input("Enter encrypted text to decrypt it: ")
text = ""

for letter in cipher_text:
    index = keys.index(letter)
    text += chars[index]

print(f"Original message: {cipher_text}")
print(f"Encrypted message: {text}")