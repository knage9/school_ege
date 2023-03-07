
for x in range(99, 1000):
    N = bin(x)[2::]
    for i in range(3):
        cal_1 = str(N).count("1")
        cal_0 = str(N).count("0")
        if cal_1 == cal_0:
            N = str(N) + str(N)[-1]
        elif cal_0 < cal_1:
            N = str(N) + "0"
        else:
            N = str(N) + "1"
    if int(N, 2) % 4 == 0:
        print(x)
        break