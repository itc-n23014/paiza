n = int(input())


def f(n):
    list = [str(i) if i != 0 else "0!!" for i in range(n + 1)[::-1]]
    return "\n".join(list)


result = f(n)
print(result)
