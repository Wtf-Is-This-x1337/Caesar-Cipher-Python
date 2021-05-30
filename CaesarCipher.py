from os import system
# Encryption Function
def cipher_encrypt(plain_text, key):
    encrypted = ""
    for c in plain_text:

        if c.isupper():
            c_index = ord(c) - ord('A')
            c_shifted = (c_index + key) % 26 + ord('A')
            c_new = chr(c_shifted)
            encrypted += c_new

        elif c.islower():
            c_index = ord(c) - ord('a') 
            c_shifted = (c_index + key) % 26 + ord('a')
            c_new = chr(c_shifted)
            encrypted += c_new

        elif c.isdigit():
            c_new = (int(c) + key) % 10
            encrypted += str(c_new)

        else:
            encrypted += c
    return encrypted

# Decryption Function
def cipher_decrypt(ciphertext, key):
    decrypted = ""
    for c in ciphertext:

        if c.isupper(): 
            c_index = ord(c) - ord('A')
            c_og_pos = (c_index - key) % 26 + ord('A')
            c_og = chr(c_og_pos)
            decrypted += c_og

        elif c.islower(): 
            c_index = ord(c) - ord('a') 
            c_og_pos = (c_index - key) % 26 + ord('a')
            c_og = chr(c_og_pos)
            decrypted += c_og

        elif c.isdigit():
            c_og = (int(c) - key) % 10
            decrypted += str(c_og)

        else:
            decrypted += c
    return decrypted

print("Caesar Cipher - WtfIsThis\n")
mode = input("Choose a mode:\n1)Encrypt text with Cipher\n2)Decrypt Text with Cipher\n3)Bruteforce the decryption key\nMode: ")
mode = int(mode)

if mode == 1:
    system('cls')
    print("\nMode Selected: 1 ->")
    shift = input("Shift pattern: ")
    shift = int(shift)
    text = input("Plain text: ")

    ### Results #1
    encrypted = cipher_encrypt(text, shift)
    print("\n\t--Results--")
    print("-> Text used: " + text)
    print("-> Shift pattern used: " + str(shift))
    print("-> Encrypted text: " + str(encrypted))
elif mode == 2:
    system('cls')
    key = input("Shift pattern used: ")
    key = int(key)
    enctext = input("The encrypted text: ")

    ### Results #2
    decrypted = cipher_decrypt(enctext, key)
    print("\n\t--Results--")
    print("-> Encrypted text used: " + enctext)
    print("-> Shift pattern used: " + str(key))
    print("-> Decrypted text: " + str(decrypted))
elif mode == 3:
    system('cls')
    brutetext = input("Encrypted text: ")
    for a in range (1,26):
        print("Shift = "+ str(a) + " | Text: " + str(cipher_decrypt(brutetext, a)))
