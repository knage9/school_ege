s = "1" * 100
while "111" in s or "88888" in s:
    if "111" in s:
        s.replace("111", "88", 1)
    else:
        s.replace("88888", "8", 1)
print(s)