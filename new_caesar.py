import string

LOWERCASE_OFFSET = ord("a")
ALPHABET = string.ascii_lowercase[:16]
#paste hereee
cipher_text = "dcebcmebecamcmanaedbacdaanafagapdaaoabaaafdbapdpaaapadanandcafaadbdaapdpandcac"

def b16_decode(encoded_text):
    decoded = ""
    for idx in range(0, len(encoded_text), 2):
      
        char1, char2 = encoded_text[idx], encoded_text[idx + 1]

        pos1, pos2 = ALPHABET.index(char1), ALPHABET.index(char2)

        binary1, binary2 = f"{pos1:04b}", f"{pos2:04b}"

        combined_binary = int(binary1 + binary2, 2)
        decoded += chr(combined_binary)
    
    return decoded

def unshift(c, key):

    shifted_index = (ALPHABET.index(c) - ALPHABET.index(key)) % len(ALPHABET)
    return ALPHABET[shifted_index]

def is_ascii(s):

    return len(s) == len(s.encode())

# Try every possible offset to see what key produces the flag.
for letter in ALPHABET:
    # d\ecrypt the cipher text with the current key
    decrypted = "".join(unshift(c, letter) for c in cipher_text)
    
    # d\ecode the b16-encoded part
    decoded_text = b16_decode(decrypted)
    
    # check
    if is_ascii(decoded_text) and " " not in decoded_text:
        print(f"Flag: picoCTF{{{decoded_text}}}")
