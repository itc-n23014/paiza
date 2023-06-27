n, m = int(input()) * 60, int(input())
t = [int(input()) for _ in range(m)]


def f(n, m, t):
    count = 0
    for i in range(m):
        n -= t[i]
        if n < 0:
            break
        count += 1
    return ("OK") if count == m else count


result = f(n, m, t)
print(result)
