def f(n, q, m, p):
    result = [
        (i, j)
        for i in range(n - m + 1)
        for j in range(n - m + 1)
        if all(q[i + i2][j + j2] == p[i2][j2] for i2 in range(m) for j2 in range(m))
    ]

    return result[0]


n = int(input())
q = [input().split() for _ in range(n)]
m = int(input())
p = [input().split() for _ in range(m)]

result = f(n, q, m, p)
print(*result)
