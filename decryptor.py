def decryptor(key, ciphertext):
    plaintext = ""
    for c in ciphertext:
        if 'a' <= c <= 'z':  # lowercase only
            newChar = ord(c) - key
            if newChar < ord('a'):
                newChar += 26
            plaintext += chr(newChar)
        else:
            # if char != to lowercase, just add it as-is
            plaintext += c
    return plaintext

ciphertext = "dmakdsymsjvas"

for i in range(1, 26):
    plaintext = decryptor(i, ciphertext)
    print("Key is:", i, "Text is:", plaintext)
