a = open("17.txt").read().splitlines()
a = list(map(int, a))
res = []
res_1 = 0
for i in range(len(a)-1):
    for x in range(i+1, len(a)):
        if ((a[i] + a[x]) % 120) == 0:
            res.append(a[i] + a[x])
print(len(res), max(res))
