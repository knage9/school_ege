
a = open("24 (5).txt").read().replace("A", "0").replace("O", "0").replace("F", "1").replace("C", "О").replace("D", "О").splitlines()
a = "".join(a)
res = []
for i in range(100):
    if "10" * i in a:
        res.append(i)
print(max(res), res)