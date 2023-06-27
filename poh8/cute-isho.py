n, m = map(int, input().split())


def f(n, m):
    return "ok" if m % n == 0 else "ng"


result = f(n, m)
print(result)
