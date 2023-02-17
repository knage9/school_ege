count = 0
def f(x, total):
    global count
    if x == total:
        count += 1
    if x < total:
        f(x + 1, total)
        f(x * 2, total)

f(2, 22)
print(count)