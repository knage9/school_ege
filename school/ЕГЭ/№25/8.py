res = []
for i in range(600_000, 600_200):
    lst = []
    for d in range(8, i//2+1):
        if str(d)[-1] == "7":
            if i % d == 0 and d != 7 and d != i:
                lst.append(d)
    if len(lst) > 0:
        print(i, lst)