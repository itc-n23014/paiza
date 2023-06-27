import math

n, p = map(int, input().split())
m, q = map(int, input().split())


def f(n, p, m, q):
    np = n * p
    pp = math.ceil(n / m) * q
    return np + pp


result = f(n, p, m, q)
print(result)
