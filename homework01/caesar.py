import typing as tp
from string import ascii_lowercase, ascii_uppercase


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
    alf_apper = ascii_uppercase + ascii_uppercase
    alf_lower = ascii_lowercase + ascii_lowercase
    ciphertext = ""
    for i in plaintext:
        if i in alf_apper:
            index = alf_apper.find(i)
            index_new = index + shift
            ciphertext += alf_apper[index_new]
        elif i in alf_lower:
            index = alf_lower.find(i)
            index_new = index + shift
            ciphertext += alf_lower[index_new]
        else:
            ciphertext += i
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
    alf_apper = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alf_lower = alf_apper.lower()
    plaintext = ""
    for i in ciphertext:
        if i in alf_apper:
            index = alf_apper.rfind(i)
            index_new = index - shift
            plaintext += alf_apper[index_new]
        elif i in alf_lower:
            index = alf_lower.rfind(i)
            index_new = index - shift
            plaintext += alf_lower[index_new]
        else:
            plaintext += i
    return plaintext


def caesar_breaker_brute_force(ciphertext: str, dictionary: tp.Set[str]) -> int:
    """
    Brute force breaking a Caesar cipher.
    """
    best_shift = 0
    # PUT YOUR CODE HERE
    return best_shift
print(decrypt_caesar(encrypt_caesar("python")))
