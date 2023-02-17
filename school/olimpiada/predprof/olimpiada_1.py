print('x1 x2 x3 f')
for x1 in [0, 1]:
    for x2 in [0]:
        for x3 in [0, 1]:
            f = x1 and (not(x2)) and x3 or (not(x1)) and x2 and x3 or x1 and (not(x2)) and x3 or x1 and x2 and (not(x3))
            print(x1, x2, x3, int(f))