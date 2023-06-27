p = [input() for _ in range(5)]


def f(p):
    return "yes" if p.count("yes") > p.count("no") else "no"


result = f(p)
print(result)
