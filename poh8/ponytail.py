d, e = zip(*(input().split() for _ in range(5)))


def f(d, e):
    count = 0
    for i in range(5):
        count += 1 if d[i] == e[i] else 0
    return "OK" if count >= 3 else "NG"


result = f(d, e)
print(result)
