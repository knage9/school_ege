for a in range(0, 300):
    k = 0
    for x in range(0, 300):
        for y in range(0, 300):
            if (2*x + 3*y > 30) or (x + y <= a):
                k += 1
    if k == 90_000:
        print(a)
        break