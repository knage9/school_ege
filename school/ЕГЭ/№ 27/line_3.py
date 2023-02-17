# import itertools
# import math
#
# a = open("27_A.txt").read().splitlines()
# a = a[1::]
#
# lst = []
# for i in range(len(a)):
#     v = a[i].split(" ")
#     v = list(map(int, v))
#     lst.append(v)
#
# max_el = -math.inf
# for item in itertools.product([0, 1, 2], repeat=len(lst)):
#     s = 0
#     for l in range(len(item)):
#         s += lst[l][item[l]]
#     if s % 91 != 0 and s > max_el:
#         max_el = s
#         print(max_el)
# print(max_el)

#способ перебора не работает так как 3**103 степени

import math

a = open("27_B.txt").read().splitlines()
a = a[1::]

lst = []
for i in range(len(a)):
    v = a[i].split(" ")
    v = sorted(list(map(int, v)))
    lst.append(v)

s_max = 0
for item in lst:
    s_max += max(item)
print(s_max)
if s_max % 91 != 0:
    print(s_max)
else:
    lst_temp = []
    for item in lst:
        s_new = s_max - item[-1] + item[1]
        if s_new % 91 != 0:
            lst_temp.append(s_new)
        s_new = s_max - item[-1] + item[0]
        if s_new % 91 != 0:
            lst_temp.append(s_new)
    print(max(lst_temp))