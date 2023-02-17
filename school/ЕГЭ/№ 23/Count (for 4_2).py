count = open("1.txt")
d = count.read().splitlines()
n = list(map(str, d))
count = 0
for i in range(len(n)):
    if "**" not in n[i]:
        count += 1
print(count)
