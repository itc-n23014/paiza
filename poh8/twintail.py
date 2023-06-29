def f(s, t):
    return "".join(["+" if i == t - 1 else "-" for i in range(s)])


s, t = int(input()), int(input())

result = f(s, t)
print(result)
