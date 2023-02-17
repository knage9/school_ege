import itertools
import math

a = open("27-A_1.txt").read().splitlines()
a = a[1::]
lst = []
for i in a:
    a, b = list(map(int, i.split()))
    lst.append([a, b])

max_el = -math.inf
for item in itertools.product([0, 1], repeat=len(lst)):
    s = 0
    for l in range(len(item)):
        s += lst[l][item[l]]
    if s % 5 != 0 and s > max_el:
        max_el = s
print(max_el)
