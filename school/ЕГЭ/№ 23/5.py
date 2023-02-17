
count = 0
def f(x, total):
    global count
    if x == total:
        count += 1
    if x > total:
        f(x - 2, total)
        f(x - 5, total)

f(23, 2)
print(count)