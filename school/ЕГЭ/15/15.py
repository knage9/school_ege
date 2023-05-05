for a in range(0, 300):
    k = 0
    for x in range(0, 300):
        for y in range(0, 300):
            if (x & 39 == 0) or ((x & 11 == 0) <= (x & a != 0)):
                k += 1
    if k == 90_000:
        print(a)
        break