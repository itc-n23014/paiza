def f(N, S):
    return "\n".join([S for _ in range(N)])


N = int(input())
S = input()

result = f(N, S)
print(result)
