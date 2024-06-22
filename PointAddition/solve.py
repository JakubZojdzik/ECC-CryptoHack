a = 497
b = 1768
p = 9739

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


X = (5274, 2841)
Y = (8669, 740)

assert add_points(X, Y) == (1024, 4440)
assert add_points(X, X) == (7284, 2107)

P = (493, 5564)
Q = (1539, 4742)
R = (4403,5202)

res = add_points(P, P)
res = add_points(res, Q)
res = add_points(res, R)

print(res)