import math

a = open("17 (1).txt").read().splitlines()
a = list(map(int, a))

res = []
res_2 = 0

min_el = []
for m in range(len(a)):
    if len(str(a[m])) == 3 and str(a[m])[-1] == "5":
        min_el.append(a[m])
min_el = min(min_el)

for i in range(len(a)-1):
    if len(str(a[i])) == 3 or len(str(a[i+1])) == 3:
        if (a[i] + a[i+1]) % min_el == 0:
            res_2 += 1
            res.append(a[i] + a[i+1])
print(res_2, len(res), min(res))