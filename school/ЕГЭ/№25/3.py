
# g = []
# for i in range(2000000, 3000000 + 1):
#     a = []
#     for v in range(1, i // 2 + 1):
#         if i % v == 0 and i // v - v >= 0 and i // v - v <= 115:
#             a.append(i//v-v)
#     if len(a) >= 3:
#         g.append(i)
# print(*sorted(g))

for x in range(2000000, 3000000+1):
    k = 0
    for i in range(1, int(x**0.5)+1):
        if x % i == 0 and abs(i - x//i) <= 115:
            k += 1
    if k >= 3:
        print(x)
