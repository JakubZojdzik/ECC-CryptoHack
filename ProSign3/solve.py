from pwn import *
import json

from ecdsa.ecdsa import Public_key, Private_key, Signature, generator_192
from Crypto.Util.number import bytes_to_long, long_to_bytes
from ecdsa.ecdsa import generator_192

FLAG = "crypto{?????????????????????????}"
g = generator_192
n = g.order()

def sha1(data):
    sha1_hash = hashlib.sha1()
    sha1_hash.update(data)
    return sha1_hash.digest()

def sign_unlock(priv_key):
    pubkey_obj = Public_key(g, g * priv_key)
    privkey_obj = Private_key(pubkey_obj, priv_key)
    msg = "unlock"
    hsh = sha1(msg.encode())
    sig = privkey_obj.sign(bytes_to_long(hsh), 420)
    return {"msg": msg, "r": hex(sig.r), "s": hex(sig.s)}

conn = remote('socket.cryptohack.org', 13381)
conn.recvline()

# Attack:
itr = 0
while(1):
    print(itr)
    itr += 1
    conn.sendline(b'{"option": "sign_time"}')
    rec = conn.recvline().decode()
    sign = json.loads(rec)
    ind = sign['msg'].find(':')
    k = 1
    r = int(sign['r'], 16)
    s = int(sign['s'], 16)
    msg = bytes_to_long(sha1(sign['msg'].encode()))

    priv_key = (((s * k - msg) % n) * pow(r, -1, n)) % n
    payload = sign_unlock(priv_key)
    payload['option'] = 'verify'
    payload = json.dumps(payload)

    conn.sendline(payload.encode())
    print(conn.recvline())