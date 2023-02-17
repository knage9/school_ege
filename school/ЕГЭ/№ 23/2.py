
def f(x, total):
    global count
    if x == total:
        count += 1
    if x < total:
        f(x + 1, total)
        f(x + 3, total)


count = 0

f(1, 9)
print(count)
count = count
count = 0
f(9, 17)
print(count)
b = count
print(count * b)