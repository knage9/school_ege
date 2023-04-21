import itertools

lst = open("18.txt").read().splitlines()
matrix = []
for m in range(len(lst)):
    matrix.append(list(map(int, lst[m].split("\t"))))
print(matrix)

s = 0
res = []
for item in itertools.product("01", repeat=18):
    x, y = 9, 0
    s = matrix[x][y]
    for t in item:
        if t == "0":
            y += 1
        else:
            x -= 1
        if x < 0 or y >= len(matrix[0]):
            break
        s += matrix[x][y]
    else:
        res.append(s)
print(sorted(res))
print(max(res), min(res))