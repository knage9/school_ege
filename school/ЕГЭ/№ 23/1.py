#

def f(x, total):
    global count
    if x == total:
        count += 1
    if x < total:
        f(x + 1, total)
        f(x + 2, total)
        f(x * 2, total)


count = 0
f(3, 10)
print(count)
count = 0
f(10, 12)
print(count)