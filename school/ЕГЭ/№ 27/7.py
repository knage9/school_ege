import itertools

for item in itertools.product("01", repeat=5):
    print("".join(item))

a = [1, 2, 3, 4]
print(max(a))