def f(s):
    c_s = ["3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A", "2"]
    o_s = [i for i in range(1, 14)]
    p_r = [0 for C in range(52)]
    p_h = [o_s[c_s.index(Card)] for Card in s]

    highest, lp_index = 0, 52
    while p_h.count(0) != 52:
        for i, n in enumerate(p_h):
            if lp_index == i:
                highest = 0
            elif n > highest:
                highest = n
                lp_index = i
                p_h[i] = 0
                p_r[i] = max(p_r) + 1

    return "\n".join([str(j) for j in p_r])


c = input().split()

result = f(c)
print(result)
