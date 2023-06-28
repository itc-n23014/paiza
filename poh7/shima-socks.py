a = int(input())
b = int(input())


def f(a, b):
    c, d, e = 1, 0, True
    f = []
    while c <= b:
        f.append("R" if e else "W")
        d += 1
        if d >= a:
            e = not e
            d = 0
        c += 1
    return "".join(f)


result = f(a, b)
print(result)
