res = 0
import itertools
for item in itertools.product("МИТРОФАН", repeat=6):
    s = "".join(item)
    s = set(s)
    t = "".join(s)
    if len(t) == 6 and "ИИ" not in t and "ОО" not in t and "АА" not in t:
        b = t.replace("Т", "М").replace("Р", "М").replace("Ф", "М").replace("Н", "М").replace("О", "И").replace("А", "М")
        if b.count("М") > b.count("И"):
            res += 1
print(res)