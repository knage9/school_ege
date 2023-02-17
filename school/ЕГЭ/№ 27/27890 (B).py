import itertools
import math

a = open("27890B.txt").read().splitlines()
a = a[1::]
lst = []
for i in a:
    a, b = list(map(int, i.split()))
    lst.append([a, b])
print(lst)
s_max = 0
for item in lst:
    s_max += max(item)
print(s_max)
if s_max % 3 != 0:
    print(s_max)
else:
    m = -math.inf
    for item in lst:
        s_new = s_max - max(item) + min(item)
        if s_new > m and s_new % 3 != 0:
            m = s_new
print(m)