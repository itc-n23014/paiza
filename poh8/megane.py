n = int(input())
a = [int(i) for i in input().split()]


def f(n, a):
    return sorted(a)[n // 2]


result = f(n, a)
print(result)
