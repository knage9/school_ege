import itertools
import math

a = open("27989_A.txt").read().splitlines()
a = a[1::]
a = list(map(int, a))
print(a)

lst = 0
for i in range(len(a)):
    for j in range(i+1, len(a)):
        if (int(a[i]) * int(a[j])) % 26 == 0 and i != j:
            lst += 1
print(lst)