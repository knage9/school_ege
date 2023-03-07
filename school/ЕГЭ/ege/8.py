import itertools
res = 0
for item in itertools.product("ABCDX", repeat=4):
    if "".join(item).count("X") == 1:
        res +=1
print(res)