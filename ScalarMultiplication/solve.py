a = 497
b = 1768
p = 9739

# Function from previous challenge
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


X = (5323, 5438)
assert multiply_points(X, 1337) == (1089, 6931)

P = (2339, 2213)
print(multiply_points(P, 7863))