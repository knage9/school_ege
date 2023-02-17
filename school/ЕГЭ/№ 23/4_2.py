
def f(x, t, arr=[""]):
    if x == t:
        print("".join(arr))
    if x <= t:
        f(x - 1, t, arr + ["+"])
        f(x + 2, t, arr + ["+"])
        f(x * 2, t, arr + ["*"])
f(1, 9)