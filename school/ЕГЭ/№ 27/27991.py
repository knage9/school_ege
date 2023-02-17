import math

a = open("27991_B.txt").read().splitlines()
a = a[1::]
a = list(map(int, a))

m = -math.inf
res = []
for i in range(len(a)):
    for j in range(len(a)):
        if (a[i] - a[j]) % 2 == 0 and (a[i]+a[j]) > m and (a[i] % 17 == 0 or a[j] % 17 == 0):
            m = a[i]+a[j]
            res.append([a[i], a[j]])
print(*res[-1])