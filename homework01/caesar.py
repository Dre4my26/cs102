import typing as tp


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
        if ord("a") <= ord(plaintext[i]) < ord("x") or ord("A") <= ord(plaintext[i]) < ord("X"):
            new_letter = ord(plaintext[i]) + shift
            ciphertext += chr(new_letter)
        elif ord("x") <= ord(plaintext[i]) <= ord("z") or ord("X") <= ord(plaintext[i]) <= ord("Z"):
            new_letter = ord(plaintext[i]) - 26 + shift
            ciphertext += chr(new_letter)
            if ord(ciphertext[i]) < ord('A') or ord('Z') < ord(ciphertext[i]) < ord('a'):
              ciphertext = ciphertext[:-1]
              ciphertext += plaintext[i]
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
    for i in range(len(ciphertext)):

        if ord("d") < ord(ciphertext[i]) < ord("z") or ord("D") <= ord(ciphertext[i]) < ord("Z"):
            new_letter = ord(ciphertext[i]) - shift
            plaintext += chr(new_letter)
        elif ord("a") <= ord(ciphertext[i]) <= ord("c") or ord("A") <= ord(ciphertext[i]) <= ord("C"):
            new_letter = ord(ciphertext[i]) - shift + 26
            plaintext += chr(new_letter)
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
