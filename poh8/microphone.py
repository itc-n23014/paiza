import math

n = int(input())
m = int(input())


def f(n, m):
    weekjob = n * 2
    return math.ceil(m / weekjob)


result = f(n, m)
print(result)
