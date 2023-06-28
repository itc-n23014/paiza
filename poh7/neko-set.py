s = input()


def f(s):
    list = [] * 4
    c, a, t = s.count("c"), s.count("a"), s.count("t")
    mn, mx = min([c, a, t]), max([c, a, t])
    list = [str(i) for i in [mn, mx - c, mx - a, mx - t]]

    return "\n".join(list)


result = f(s)
print(result)
