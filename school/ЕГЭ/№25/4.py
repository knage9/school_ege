for x in range(101000000, 102000000+1, 2):
    k = 0
    for i in range(2, int(x**0.5)+1, 2):
        if x % i == 0:
            k += 1
    if k == 3:
        print(x)
