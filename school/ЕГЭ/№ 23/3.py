
def f(x, total):
    global count
    if x == total:
        count += 1
    if x < total:
        f(x + 2, total)
        f(x * 2, total)

count = 0
f(1, 18)
count = count
count = 0
f(18, 52)
b = count
print(count * b)