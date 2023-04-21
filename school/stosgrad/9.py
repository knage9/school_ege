# from collections import Counter
a = open("1.txt").read().replace("\t", " ").splitlines()
# m = []
# for i in a:
#     b = i.split(" ")
#     for v in range(len(b)):
#         m.append(b[v])
# print(Counter(m).most_common())
#('135', 46), ('654', 46), ('504', 46), ('597', 46), ('291', 46), ('562', 46), ('852', 46), ('785', 46), ('368', 46), ('232', 46)

def f(o):
    for k in range(len(o)):
        if o[k] == "135" or o[k] == "654" or o[k] == "504" or o[k] == "597" or o[k] == "291" or o[k] == "562" or o[k] == "852" \
                or o[k] == "785" or o[k] == "368" or o[k] == "232":
            if o.count(o[k]) == 1:
                return 1
        else:
            return 0

res = 0
for i in a:
    b = i.split(" ")
    res += f(b)
print(res)
