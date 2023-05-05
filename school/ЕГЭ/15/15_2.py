import math

a_min = []
for a1 in range(0, 300):
    for a2 in range(a1 + 1, 300):
        m = True
        A = a2 - a1
        for x in range(0, 300):
            d = (17 <= x <= 54) <= (((37 <= x <= 83) and (not(a1 <= x <= a2))) <= (not(17 <= x <= 54)))
            if d == False:
                m = False
                break
        if m:
            a_min.append(A)
print(min(a_min))


