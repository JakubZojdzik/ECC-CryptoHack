#!/usr/bin/env python3
import fastecdsa
from fastecdsa.point import Point
from pwn import *


G = fastecdsa.curve.P256.G
assert G.x, G.y == [0x6B17D1F2E12C4247F8BCE6E563A440F277037D812DEB33A0F4A13945D898C296,
                    0x4FE342E2FE1A7F9B8EE7EB4A7C0F9E162BCE33576B315ECECBB6406837BF51F5]


p = fastecdsa.curve.P256.p
q = fastecdsa.curve.P256.q
target = Point(0x3B827FF5E8EA151E6E51F8D0ABF08D90F571914A595891F9998A5BD49DFA3531, 0xAB61705C502CA0F7AA127DEC096B2BBDC9BD3B4281808B3740C320810888592A)

# https://crypto.stackexchange.com/questions/55069/elliptic-curve-divide-by-2#answer-55109
i = pow(2, -1, q)
P = target * i

conn = remote('socket.cryptohack.org', 13382)
conn.recvline()

payload = '{"host": "www.bing.pl", "private_key": 2, "generator": [' + str(P.x) + ',' + str(P.y) + '], "curve": "secp256r1"}'

conn.sendline(payload.encode())
print(conn.recvline())