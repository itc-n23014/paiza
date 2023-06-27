N = int(input())


def f(N):
    return "lucky" if N % 7 == 0 else "unlucky"


result = f(N)
print(result)
