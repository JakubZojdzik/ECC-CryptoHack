from sage.all import *
from Crypto.Cipher import AES
import hashlib

def decrypt_flag(shared_secret: int):
    sha1 = hashlib.sha1()
    sha1.update(str(shared_secret).encode('ascii'))
    key = sha1.digest()[:16]

    iv = bytes.fromhex('07e2628b590095a5e332d397b8a59aa7')
    ciphertext = bytes.fromhex('8220b7c47b36777a737f5ef9caa2814cf20c1c1ef496ec21a9b4833da24a008d0870d3ac3a6ad80065c138a2ed6136af')
    cipher = AES.new(key, AES.MODE_CBC, iv)

    # Prepare data to send
    pt = cipher.decrypt(ciphertext)
    return pt

# Define curve
p = 310717010502520989590157367261876774703
a = 2
b = 3
F = GF(p)
EC = EllipticCurve(F, [a, b])

G = EC(179210853392303317793440285562762725654, 105268671499942631758568591033409611165)

# Q = n1 * G
Q = EC(280810182131414898730378982766101210916, 291506490768054478159835604632710368904)

# B = n2 * G
B = EC(272640099140026426377756188075937988094, 51062462309521034358726608268084433317)


# Pohlig Hellman
ordG = G.order()
factors = factor(ordG)
smallres = []
smallmod = []
for f in factors:
    smallmod.append(f[0]^f[1])
    curr = ordG // (f[0]^f[1])
    Q2 = curr * Q
    P2 = curr * G
    if(f[1] != 1):
        smallres.append(discrete_log(Q2, P2, operation='+'))
    else:
        smallres.append(discrete_log_rho(Q2, P2, operation='+'))

# Chinese Remainder Theorem
n1 = crt(smallres, smallmod)
assert n1*G == Q

# Shared secret = Q * n2 = B * n1 = G * n1 * n2
print(decrypt_flag((n1*B)[0]))
