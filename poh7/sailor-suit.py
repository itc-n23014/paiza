n = int(input())
s = [input() for _ in range(n)]


def f(s):
    return "_".join(s)


result = f(s)
print(result)
