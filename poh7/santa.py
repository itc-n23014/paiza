def f(X, Y, Z, N, d):
    cut = [[0, X], [0, Y]]
    for i in range(N):
        dire, long = d[i]
        cut[dire].append(long)

    min_v = [X, Y]
    for i in range(2):
        cut[i].sort()
        for j in range(1, len(cut[i])):
            min_v[i] = min(min_v[i], cut[i][j] - cut[i][j - 1])

    return min_v[0] * min_v[1] * Z


X, Y, Z, N = map(int, input().split())
d = [list(map(int, input().split())) for _ in range(N)]

result = f(X, Y, Z, N, d)
print(result)
