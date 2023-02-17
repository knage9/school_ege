# a = open("data.txt").read().split()
# res = 0
# for i in range(len(a)):
#     res += int(a[i])
# print(res)
import math

# a = open("data.txt").read().splitlines()
# a = list(map(int, a))
# print(sum(a))

a = open("27-A_demo.txt").read().splitlines()
a = a[1::]
lst = []
print(a)
for i in a:
    a, b = map(int, i.split())
    lst.append([a, b])
print(lst)

import itertools

m = -math.inf
for item in itertools.product([0, 1], repeat=len(lst)):
    s = 0
    for i in range(len(item)):
        s += lst[i][item[i]]
    if s % 3 != 0:
        if s > m:
            m = s
print(m)