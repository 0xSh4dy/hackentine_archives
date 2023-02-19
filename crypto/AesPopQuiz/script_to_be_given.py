from Crypto.Cipher import AES
from os import urandom
flag_p1 = "redacted"
fake_answer = 5 #Obviously wrong!
print("Before you go into 'breaking' AES, let's warm you up with some basic questions. Shall we?")

print("As which type of cipher can AES be used as?")
print("1. Block cipher")
print("2. Stream cipher")
print("3. Both")
if (a == fake_answer):
    print("Correct! Lets move forward.")
else:
    print("Wrong! I don't think that you have done enough work. Bye!")
    exit(0)

print("Which attack on AES involves hardware implementation of AES?")
print("1. Differential cryptanalysis")
print("2. Linear cryptanalysis")
print("3. Side channel attack")
print("4. Interpolation attack")
a = int(input("Enter your answer: "))
if (a == fake_answer):
    print("Correct! Lets move forward.")
else:
    print("Wrong! I don't think that you have done enough work. Bye!")
    exit(0)
        
print("What are the two properties related to AES?")
print("1. Dellusion and confusion")
print("2. Confusion and diffusion")
print("3. Diffusion and dellusion")
a = int(input("Enter your answer: "))
if (a == fake_answer):
    print("Correct! Lets move forward.")
else:
    print("Wrong! I don't think that you have done enough work. Bye!")
    exit(0)

print("Which attack on AES reduced its security, although it was not a practical attack?")
print("1. Coppersmith's attack")
print("2. Biclique attack")
print("3. Saturation attack")
a = int(input("Enter your answer: "))
if (a == fake_answer):
    print("Correct! Lets move forward.")
else:
    print("Wrong! I don't think that you have done enough work. Bye!")
    exit(0)
        
print(f"Looks like you have done enough work. Here's a part of your flag: '{flag_p1}'")

block_size = 16
key = urandom(block_size)
flag_p2 = "redacted"
def pad(plaintext):
    padded = plaintext
    i = 0
    while (len(padded) % block_size != 0):
        padded += flag_p2[i]
        i += 1
    return padded[::-1]
   
iv=urandom(block_size) 
def encrypt(plaintext):
    cipher = AES.new(key, AES.MODE_ECB)
    return cipher.encrypt(pad(plaintext).encode())

encrypted_flag = encrypt(flag_p2)
print("Looks like you encountered a hurdle. Pass it to get a chance to go on a candle light dinner with me. Wink! Wink!")
print("But lemme give you the encrypted version of a part of the flag in hex: "+encrypted_flag.hex())
print("Actions: 1. Encrypt 2. Check flag part 3. Exit")
while True:
    a = int(input("Enter action: "))
    if (a == 1):
        print("Enter the plaintext: ")
        pt = input()
        print("Here you go darling "+encrypt(pt).hex())        
    elif (a == 2):
        flag_ch = input("Enter flag part to be verified(as ascii string only): ")
        if (flag_ch == flag_p2):
            print("Congrats! Lets move to the next level.")
            break
        else:
            print("Oops, that's not the right one. Try again")
    elif (a == 3):
        print("Looks like you are not interested. Bye!")
        exit(0)
    else:
        print("Stay within your limits. Bye!")
        exit(0)

flag_p3 = "redacted"

key = urandom(block_size)

def encrypt2(plaintext):
    while (len(plaintext) % block_size != 0):
        plaintext += flag_p3[len(plaintext)]
    iv=urandom(block_size)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    ct = cipher.encrypt2(plaintext.encode())
    return iv.hex()+ct.hex()

def decrypt(ciphertext):
    ciphertext = bytes.fromhex(ciphertext)
    cipher = AES.new(key, AES.MODE_ECB)
    try:
        decrypted = cipher.decrypt(ciphertext)
    except ValueError as e:
        return "Error: " + str(e)
    return "Plaintext: " + decrypted.hex()

print("Looks like you have done a lot of hard work to reach here. No issues, 'tis the last level. You may not get a date from Connect-E-Dil, but will surely get the flag from me!")
print("Actions: 1. Encrypt in AES CBC mode 2. Decrypt in AES EBC mode 3. Exit")
while True:
    a = int(input("Enter action: "))
    if (a == 1):
        print("Enter the plaintext: ")
        print("Here you go darling (the first 16 bytes are the initialization vector and the rest is the ciphertext): "+encrypt2(input()))
    elif (a == 2):
        print("Enter the ciphertext: ")
        print(decrypt(input()))
    elif (a == 3):
        print("Have you got the flag or do you wanna quit? Anyways, bye!")
        exit(0)
    else:
        print("Stay within your limits. Bye!")
        exit(0)
