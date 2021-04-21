from hashlib import sha256
import random

def get_hexdigest(salt, plaintext):
    return sha256((salt + plaintext).encode('utf-8')).hexdigest()

SECRET_KEY = 's3cr3t'

def make_password(plaintext, user_name):
    salt = get_hexdigest(SECRET_KEY, user_name)[:20]
    hsh = get_hexdigest(salt, plaintext)
    return ''.join((salt, hsh))


def password(plaintext, user_name, length = 10):
    raw_hexdigest = make_password(plaintext, user_name)
    ALPHABET = ('abcdefghijklmnopqrstuvwxyz', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', '0123456789!@#$%^&*()-_')


    num = int(raw_hexdigest, 16)

    chars = []
    while len(chars) < length:
        n = random.randint(0, len(ALPHABET)-1)
        alpha = ALPHABET[n]
        n = random.randint(0, len(alpha)-1)
        chars.append(alpha[n])

    return ''.join(chars)
