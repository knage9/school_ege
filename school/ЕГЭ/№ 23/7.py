
def f(x, total):
    global count
    if x == total:
        count += 1
    if x == 26:
        return
    if x < total:
        f(x + 1, total)
        f((2 * x)+1, total)

count = 0
f(1, 27)
print(count)
