def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.

    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    ciphertext = ""
    for i in range(len(plaintext)):
      letter_new = ord(plaintext[i])
      key = ord(keyword[i % len(keyword)])
      if letter_new >= ord('A') and letter_new <= ord('Z'):
        if key >= ord('A') and key <= ord('Z'):
          ciphertext += chr((letter_new - ord('A') + key - ord('A')) % 26 + ord('A'))
        else:
          ciphertext += chr((letter_new + key - ord('A') - ord('a')) % 26 + ord('A'))
      elif letter_new >= ord("a") and letter_new <= ord("z"):
        if key>= ord('A') and key <= ord('Z'):
          ciphertext += chr((letter_new + key - ord('a') - ord('A')) % 26 + ord('a'))
        else:
          ciphertext += chr((letter_new - ord('a') + key - ord('a')) % 26 + ord('a'))
      else:
        ciphertext += chr(letter_new)
    return ciphertext

def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.

    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    plaintext = ""
    for i in range(len(ciphertext)):
      letter_new = ord(ciphertext[i])
      key = ord(keyword[i % len(keyword)])
      if letter_new >= ord('A') and letter_new <= ord('Z'):
        if key >= ord('A') and key <= ord('Z'):
          plaintext += chr((letter_new - ord('A') - key + ord('A')) % 26 + ord('A'))
        else:
          plaintext += chr((letter_new - ord('A ') - key + ord('a')) % 26 + ord('A'))
      elif letter_new >= ord('a') and letter_new <= ord('z'):
        if key >= ord('A') and key <= ord('Z'):
          plaintext += chr((letter_new - ord('a') - key + ord('A')) % 26 + ord('a'))
        else:
          plaintext += chr((letter_new - ord('a') - key + ord('a')) % 26 + ord('a'))
    return plaintext