n = int(input())
m1 = int(input())
x = list(map(int, input().split()))
m2 = int(input())
y = list(map(int, input().split()))


def f(x, y):
    list1 = sorted([int(i) for i in y if i not in x])
    list2 = [str(i) for i in list1]
    return " ".join(list2) if len(list2) != 0 else None


result = f(x, y)
print(result)
