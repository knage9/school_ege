import itertools

res = 0
ma = []
for item in itertools.product("01234567", repeat=5):
    a = "".join(item)
    if a.count("6") == 1 and a[0] != "0":
        ma.append(a)

for i in ma:
    b = i.split("6")
    if b[0] != "" and b[-1] != "" and int(b[0][-1]) % 2 == 0 and int(b[-1][0]) % 2 == 0:
        res += 1
    elif b[0] == "" and int(b[-1][0]) % 2 == 0:
        res += 1
    elif b[-1] == "" and int(b[0][-1]) % 2 == 0:
        res += 1
print(res)