import itertools
import math

a = open("27-A_1.txt").read().splitlines()
a = a[1::]
lst = []
for i in a:
    a, b = list(map(int, i.split()))
    lst.append([a, b])
print(lst)

max_el = -math.inf
lst2 = []
s = 0
for x in lst:
    print(sorted(x)[-1])