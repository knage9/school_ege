def f(x, total):
    global count
    if x == total:
        count += 1
    if x == 17:
        return
    if x < total:
        f(x + 1, total)
        f(x * 2, total)

count = 0
f(1, 10)
print(count)
count = count
count = 0
f(10, 35)
print(count)
b = count
print(count * b)