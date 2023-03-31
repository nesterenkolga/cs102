from string import ascii_lowercase, ascii_uppercase


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
    alf_apper = ascii_uppercase + ascii_uppercase
    alf_lower = ascii_lowercase + ascii_lowercase
    keyword_full = ""
    ciphertext = ""
    for i in range(0, len(plaintext)):
        index = i % len(keyword)
        keyword_full += keyword[index]
    for i in range(0, len(plaintext)):
        if plaintext[i] in alf_apper:
            index = alf_apper.find(plaintext[i]) + alf_apper.find(keyword_full[i])
            ciphertext += alf_apper[index]
        elif plaintext[i] in alf_lower:
            index = alf_lower.find(plaintext[i]) + alf_lower.find(keyword_full[i])
            ciphertext += alf_lower[index]
        else:
            ciphertext += plaintext[i]
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
    alf_apper = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alf_lower = alf_apper.lower()
    keyword_full = ""
    plaintext = ""
    for i in range(0, len(ciphertext)):
        index = i % len(keyword)
        keyword_full += keyword[index]
    for i in range(0, len(ciphertext)):
        if ciphertext[i] in alf_apper:
            index = alf_apper.find(ciphertext[i]) - alf_apper.find(keyword_full[i])
            plaintext += alf_apper[index]
        elif ciphertext[i] in alf_lower:
            index = alf_lower.find(ciphertext[i]) - alf_lower.find(keyword_full[i])
            plaintext += alf_lower[index]
        else:
            plaintext += ciphertext[i]
    return plaintext
