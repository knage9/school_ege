res_2 = []
for N in range(1, 1000):
    N = bin(N)[2::]
    b = str(N)[-1]
    N = str(N) + b
    sum_l = 0
    for i in range(len(N)):
        sum_l += int(N[i])
    N = str(N) + str(int(sum_l) % 2)
    res = int(N, 2)
    if res > 105:
        res_2.append(res)
print(res_2[0])