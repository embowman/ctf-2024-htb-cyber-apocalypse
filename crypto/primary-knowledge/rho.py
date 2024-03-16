import math

def pollard_rho(n):
    x = 2
    y = 2
    d = 1

    while d == 1:
        x = (x**(2) + 1) % n
        y = ((y**2 + 1)**2 + 1) % n
        d = math.gcd(abs(x - y), n)

    if d == n:
        return 0
    else:
        return d
    
num = 17 * 97
result = pollard_rho(num)
print(result)