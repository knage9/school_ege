import itertools


for item in itertools.product("1289", repeat=2):
    k = [6, 9]
    for step in item:
        if step == "1":
            k[0] += 1
        if step ==  "2":
            k[1] += 1
        if step == "8":
            k[0] *= 2
        if step == "9":
            k[1] *= 2
    print(item, k)