import random, time

def encrypt(plaintext, key):
  alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
  ciphertext = ""
  for i in range(0,len(plaintext)):
    character = plaintext[i]
    ciphertext = ciphertext + character
    for j in range (0,key):
      ciphertext = ciphertext + random.choice(alphabet)
  return ciphertext

plaintext = input("Enter a message to encrypt (plaintext): ")
key = int(input("Input a key as a number between 1 and 10: "))
while not (key >= 1 and key <= 10):
  print("Invalid key, try again!")
  key = int(input("Input a key as a number between 1 and 10: "))

print("...")
time.sleep(1)
print("Encrypting plaintext")
time.sleep(1)
print("...")
time.sleep(1)
ciphertext = encrypt(plaintext, key)

print("Ciphertext:")
print(ciphertext)