def f(x, total):
    global count
    if x == total:
        count += 1
    if x == 5 or x == 10:
        return
    if x < total:
        f(x + 1, total)
        f(x * 2, total)
        f(x + 3, total)

count = 0
f(2, 14)
print(count)