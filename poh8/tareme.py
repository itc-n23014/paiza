def f(s, n):
    return "OK" if s >= n else "NG"


s, n = map(int, input().split())

result = f(s, n)
print(result)
