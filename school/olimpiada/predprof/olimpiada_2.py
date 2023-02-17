import itertools

gla = "aeyuioюэия"
sog = "qwrtpsdf"
s = gla + sog

count = 0
for el in itertools.product(s, repeat=6):
    s_el = "".join(el)
    count_gla = 0
    count_sog = 0
    for letter in set(list(s_el)):
        if letter in gla:
            count_gla += 1
        if letter in sog:
            count_sog += 1
    if count_gla == 4 and count_sog == 2:
        count += 1

print(count)