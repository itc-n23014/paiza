def f(d, e):
    count = sum(1 for i in range(5) if d[i] == e[i])
    return "OK" if count >= 3 else "NG"


d, e = zip(*(input().split() for _ in range(5)))

result = f(d, e)
print(result)
