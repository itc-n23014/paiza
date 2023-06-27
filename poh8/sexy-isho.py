m, n = map(int, input().split())


def f(m, n):
    return m - n if m > n else 0


result = f(m, n)
print(result)
