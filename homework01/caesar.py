import typing as tp
import string


def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    """
    Encrypts plaintext using a Caesar cipher.

    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    ciphertext = ""
    for i in range(len(plaintext)):
        if ord('A') <= ord(plaintext[i]) <= ord('Z'):
            if ord('Z') - ord(plaintext[i]) < shift:
                ciphertext += chr(ord('A') - 1 + (shift - ord('Z') + ord(plaintext[i])))
            else:
                ciphertext += chr(ord(plaintext[i]) + shift)
        elif ord('a') <= ord(plaintext[i]) <= ord('z'):
            if ord('z') - ord(plaintext[i]) < shift:
                ciphertext += chr(ord('a') - 1 + (shift - ord('z') + ord(plaintext[i])))
            else:
                ciphertext += chr(ord(plaintext[i]) + shift)
        else:
            ciphertext += plaintext[i]
          
    return ciphertext


def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    """
    Decrypts a ciphertext using a Caesar cipher.

    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    plaintext = ""
    for i in range (len(ciphertext)):
        if ord('A') <= ord(ciphertext[i]) <= ord('Z'):
            if ord(ciphertext[i]) - shift < ord('A'):
                plaintext += chr(ord('Z') + 1 - (shift - (ord(ciphertext[i]) - ord('A'))))
            else:
                 plaintext += chr(ord(ciphertext[i]) - shift)
        
        elif ord('a') <= ord(ciphertext[i]) <= ord('z'):
            if ord(ciphertext[i]) - shift < ord('a'):
                plaintext += chr(ord('z') + 1 - (shift-(ord(ciphertext[i]) - ord('a'))))
            else:
                 plaintext += chr(ord(ciphertext[i]) - shift)
        else:
            plaintext += ciphertext[i]

    return plaintext


def caesar_breaker_brute_force(ciphertext: str, dictionary: tp.Set[str]) -> int:
    """
    Brute force breaking a Caesar cipher.
    """
    best_shift = 0
    # PUT YOUR CODE HERE
    return best_shift
