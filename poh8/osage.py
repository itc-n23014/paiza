def f(n, m, t):
    count = sum(1 for i in range(m) if (n := n - t[i]) >= 0)
    return "OK" if count == m else count


n, m = int(input()) * 60, int(input())
t = [int(input()) for _ in range(m)]

result = f(n, m, t)
print(result)
