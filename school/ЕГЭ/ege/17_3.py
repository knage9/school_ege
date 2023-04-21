import math

a = open("17 (1).txt").read().splitlines()
a = list(map(int, a))

max_el = -math.inf
for m in range(len(a)):
    if a[m] > max_el and str(a[m])[-1] == "3":
        max_el = a[m]

res = []
for i in range(len(a)-1):
    if (str(a[i])[-1] == "3" and str(a[i+1])[-1] != "3") or (str(a[i+1])[-1] == "3" and str(a[i])[-1] != "3"):
        if (a[i]**2 + a[i+1]**2) >= max_el**2:
            res.append(a[i]**2 + a[i+1]**2)
print(len(res), max(res))