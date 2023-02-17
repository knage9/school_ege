g = []
for i in range(123456789, 223456789 + 1):
    count = []
    if int(i**0.5)**2 == i:
        for v in range(2, int(i**0.5)-1):
            if i % v == 0:
                count.append(v)
        if len(count) == 1:
            print(i, i // count[-1])