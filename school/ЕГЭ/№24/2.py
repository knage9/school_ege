s = open("1.txt").readline()
d = dict()

for i in range(26):
    d[chr(ord("A") + i)] = 0

for i in range(26):
    e = "E" + chr(ord("A") + i)
    d[chr(ord("A") + i)] = s.count(e)

print(d)
print(max(d.values()))