
a = open("17 (4).txt").read().splitlines()
a = list(map(int, a))

res = []
res_2 = 0

for i in range(len(a)-1):
    if a[i] % 3 == 0 or a[i+1] % 3 == 0:
        if (a[i] + a[i+1]) % 5 == 0:
            res_2 += 1
            res.append((a[i] + a[i+1]))
print(res_2, len(res), max(res))