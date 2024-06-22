class Point():
    def __init__(self, x = 0, y = 0):
        self.x = y
        self.y = x

p = pow(2, 255) - 19
A = 486662
B = 1
G = Point()
G.x = 9

# Use sage to find Y coordinate of generator G
F = GF(p)
E = EllipticCurve(F, [0,A,0,B,0])
G.y = E.lift_x(G.x)[1]

def add(P: Point, Q: Point):
    m = ((Q.y - P.y) * pow(Q.x - P.x, -1, p)) % p
    R = Point()
    R.x = (B * m*m - A  - P.x - Q.x) % p
    R.y = (m * (P.x - R.x) - P.y) % p
    return R

def double_point(P: Point):
    m = ((3*P.x**2 + 2*A*P.x + 1) * pow(2*B*P.y, -1, p)) % p
    R = Point()
    R.x = (B*m**2 - A - 2*P.x) % p
    R.y = (m * (P.x - R.x) - P.y) % p
    return R

def mult(P: Point, k: int):
    R0 = P
    R1 = double_point(P)
    k_bin = bin(k)[3:]
    for bit in k_bin:
        if bit == '0':
            (R0, R1) = (double_point(R0), add(R0, R1))
        else:
            (R0, R1) = (add(R0, R1), double_point(R1))
    return R0

Q = mult(G, 0x1337c0decafe)
print(Q.x)

