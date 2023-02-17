jordan = list(map(int, input().split()))

cherk = [hum for hum in jordan if hum != -1]
cherk = sorted(cherk)

netrofalse = []
for i in range(len(jordan)):
    if jordan[i] == -1:
        netrofalse.append(-1)
    else:
        netrofalse.append(cherk[0])
        cherk = cherk[1:]

print(*netrofalse, sep=" ")