def f(n, t):
    c, d = 0, 0
    for i in range(24):
        for j in range(n):
            if int(t[j][0]) == i:
                if t[j][1] == "in":
                    c += 5
                if t[j][1] == "out":
                    c += 3

        if c <= 0:
            d += 1
        if c > 0:
            d += 2
            c -= 1

    return d


n = int(input())
t = [list(input().split()) for _ in range(n)]

result = f(n, t)
print(result)
