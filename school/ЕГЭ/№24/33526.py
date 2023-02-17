s = open("2.txt").readline()
d = dict()
for i in range(26):
    d[chr(ord("A") + i)] = 0
for i in range(26):
    for t in range(26):
        e = chr(ord("A") + t) + chr(ord("A") + i) + chr(ord("A") + t)
        d[chr(ord("A") + i)] = s.count(e)
print(d)
print(max(d.values()))
for k, v in d.items():
    if v == max(d.values()):
        print(k)