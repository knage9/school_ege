count = list(map(int, input().split()))
s = []
index = ""
for i in range(len(count)):
    if count[i] != -1:
        s.append(count[i])
    if count[i] == -1:
        index += str(i)
s = sorted(s)
for x in range(len(index)):
    g = int(index[x])
    s.insert(g, -1)
print(*s, sep=" ")