x = 49**6 + 7**19 - 21
s = ""
while x != 0:
    s += str(x % 7)
    x //= 7
s = s[::-1]
print(s.count("0"))