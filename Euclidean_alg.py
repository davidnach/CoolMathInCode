def gcd(a,b):
    if b == 0:
        return a
    r = a % b
    while r != 0:
        a = b
        b = r
        r = a % b
    return b

print(gcd(150,100))
