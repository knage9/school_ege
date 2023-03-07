res = []
for a in range(100, 1000):
    a = str(a)
    b = int(a[0]) + int(a[1])
    c = int(a[1]) + int(a[2])
    res.append([b, c])
res_1 = 0
for i in range(len(res)):
    b = sorted(res[i])
    if str(b[1]) + str(b[0]) == "1715":
        res_1 += 1
print(res_1)