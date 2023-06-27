N = int(input())
S = input()


def f(N, S):
    return "\n".join([S for _ in range(N)])


result = f(N, S)
print(result)
