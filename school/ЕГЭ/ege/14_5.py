x = 3*(343**8) + 5*(49**12) + 7**15 - 49
s = ""
while x != 0:
    s += str(x % 7)
    x //= 7
s = s[2::]
print(s.count("6"), s.count("0"))