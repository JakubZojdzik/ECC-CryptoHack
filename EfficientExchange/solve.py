from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import hashlib


def is_pkcs7_padded(message):
    padding = message[-message[-1]:]
    return all(padding[i] == len(padding) for i in range(0, len(padding)))


def decrypt_flag(shared_secret: int, iv: str, ciphertext: str):
    # Derive AES key from shared secret
    sha1 = hashlib.sha1()
    sha1.update(str(shared_secret).encode('ascii'))
    key = sha1.digest()[:16]
    # Decrypt flag
    ciphertext = bytes.fromhex(ciphertext)
    iv = bytes.fromhex(iv)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = cipher.decrypt(ciphertext)

    if is_pkcs7_padded(plaintext):
        return unpad(plaintext, 16).decode('ascii')
    else:
        return plaintext.decode('ascii')


# Functions from previous challenges
def add_points(P, Q):
    if(P == (0, 0)):
        return Q
    if(Q == (0, 0)):
        return P

    x1, y1 = P
    x2, y2 = Q
    if(x1 == x2 and y1 == -y2):
        return (0, 0)

    if(P != Q):
        lamb = (y2 - y1) * pow((x2 - x1), -1, p)
    if(P == Q):
        lamb = (3*x1**2 + a) * pow(2*y1, -1, p)
    x3 = lamb**2 - x1 - x2
    y3 = lamb * (x1-x3) - y1
    return (x3%p, y3%p)

def multiply_points(P, n):
    Q = P
    R = (0, 0)

    while(n > 0):
        if(n % 2 == 1):
            R = add_points(R, Q)
        Q = add_points(Q, Q)
        n = n//2
    return R

a = 497
b = 1768
p = 9739

q_x = 4726

# y**2 coordinate of point Q
q_y2 = q_x**3 + a*q_x + b

# it is so easy thanks to p ≡ 3 mod 4
q_y = pow(q_y2, ((p + 1) // 4), p)

Q = (q_x, q_y)

nB = 6534

P = multiply_points(Q, nB)


shared_secret = P[0]
iv = 'cd9da9f1c60925922377ea952afc212c'
ciphertext = 'febcbe3a3414a730b125931dccf912d2239f3e969c4334d95ed0ec86f6449ad8'

print(decrypt_flag(shared_secret, iv, ciphertext))
