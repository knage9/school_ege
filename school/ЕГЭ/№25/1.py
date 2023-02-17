import math

g = []
max_el = -math.inf
for i in range(84052, 84130 + 1):
    s = []
    for v in range(1, i + 1):
        if i % v == 0:
            s.append(v)
        if len(s) > max_el:
            max_el = len(s)
            g.append([max_el, v])

print(*g[-1])