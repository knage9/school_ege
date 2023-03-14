import itertools

imp = set()
for item in itertools.permutations("ПАРАБОЛА"):
    a = "".join(item)
    b = a.replace("О", "А").replace("Р", "П").replace("Б", "П").replace("Л", "П")
    if "АА" not in b and "ПП" not in b:
        imp.add(a)
print(len(imp))