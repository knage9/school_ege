res = []
for a1 in range(0, 300):
    for a2 in range(a1+1, 300):
        m = True
        A = a2 - a1
        for x in range(0, 300):
            d = (77 <= x <= 114) <= (((69 <= x <= 91) == (77 <= x <= 114)) or ((not(69 <= x <= 91)) <= (a1 <= x <= a2)))
            if d == False:
                m = False
                break
        if m:
            res.append(A)
print(min(res))