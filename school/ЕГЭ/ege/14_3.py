
res = []
for x in range(1, 11):
    for y in range(1, 11):
        for x_2 in range(1, 8):
            for y_2 in range(1, 8):
                s_1 = int(str(y) + '04' + str(x) + '5', 11)
                s_2 = int('253' + str(x_2) + str(y_2), 8)
                s = int(s_1) + int(s_2)
                if s % 117 == 0:
                    res.append(s)
print(min(res) // 117)