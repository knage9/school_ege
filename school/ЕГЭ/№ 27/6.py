import math

a = open("27_B (1).txt").read().splitlines()
a = a[1::]

lst = []
for i in range(len(a)):
    v = a[i].split(" ")
    v = list(map(int, v))
    lst.append(v)

s_max = 0
for item in lst:
    s_max += max(item)
print(s_max)
if s_max % 13 != 0:
    print(s_max)
else:
    m = -math.inf
    for item in lst:
        s_new = s_max - max(item) + min(item)
        if s_new > m and s_new % 13 != 0:
            m = s_new
    print(m)