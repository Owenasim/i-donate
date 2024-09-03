import os
from base64 import b64decode, b64encode

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes


def generate_key():
    return os.urandom(32)


def encrypt(plaintext, key):
    iv = os.urandom(12)

    cipher = Cipher(algorithms.AES(key), modes.GCM(iv), backend=default_backend())
    encryptor = cipher.encryptor()

    ciphertext = encryptor.update(plaintext.encode()) + encryptor.finalize()

    return b64encode(iv + encryptor.tag + ciphertext).decode("utf-8")


def decrypt(ciphertext, key):
    decoded = b64decode(ciphertext.encode())
    iv = decoded[:12]
    tag = decoded[12:28]
    ciphertext = decoded[28:]
    cipher = Cipher(algorithms.AES(key), modes.GCM(iv, tag), backend=default_backend())
    decryptor = cipher.decryptor()
    return (decryptor.update(ciphertext) + decryptor.finalize()).decode("utf-8")
