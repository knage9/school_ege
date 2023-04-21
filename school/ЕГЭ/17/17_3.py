import math

a = open("17 (3).txt").read().splitlines()
a = list(map(int, a))

res = []
res_2 = 0

min_el = []
for m in range(len(a)):
    if str(a[m])[-1] == "7":
        min_el.append(a[m])
min_el = min(min_el)**2

for i in range(len(a)-1):
    if (str(a[i])[-1] == "7" and str(a[i+1])[-1] != "7") or (str(a[i])[-1] != "7" and str(a[i+1])[-1] == "7"):
        if ((a[i]**2) + (a[i+1]**2)) < min_el:
            res_2 += 1
            res.append((a[i]**2) + (a[i+1]**2))
print(res_2, len(res), max(res))