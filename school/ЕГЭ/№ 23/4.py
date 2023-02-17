#4681
def f(x, total, b=True, last=None):
    global count
    if x == total and b:
        count += 1
    if x < total:
        f(x + 1, total, b, "+")
        f(x + 2, total, b, "+")
        if last == "*":
            f(x * 2, total, False, "*")
        else:
            f(x * 2, total, b, "*")

count = 0
f(1, 11)
print(count)