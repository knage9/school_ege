import math

a = open("27-A_2 (1).txt").read().splitlines()
a = a[1::]
a = list(map(int, a))

m = -math.inf
for i in range(len(a)):
    for j in range(len(a)):
        if (a[i]*a[j]) % 14 == 0 and (a[i]*a[j]) > m:
            m = a[i]*a[j]
print(m)