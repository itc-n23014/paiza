p = int(input())


def f(p):
    return p // 100 + 10 if p >= 1000 else p // 100


result = f(p)
print(result)
