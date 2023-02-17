#2**n · p**4
def f(x):
    for i in range(2, (x // 2) + 1):
        if x % i == 0:
            return False
    return True


for x in range(35000000, 40000000 + 1):
    xb2 = x
    while xb2 % 2 == 0:
        xb2 /= 2
    if int(xb2 ** 0.25)**4 == xb2:
        if f(int(xb2 ** 0.25)) == True:
            print(x)
