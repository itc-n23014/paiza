c1, p1 = map(int, input().split())
c2, p2 = map(int, input().split())


def f(c1, p1, c2, p2):
    return 1 if c1 / p1 > c2 / p2 else 2


result = f(c1, p1, c2, p2)
print(result)
