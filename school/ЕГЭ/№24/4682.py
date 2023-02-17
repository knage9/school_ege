s = open("24 (3).txt").readline()

s = s.replace('A', '1').replace('E', '1').replace('B', '0').replace('C', '0').replace('D', '0')
for i in range(1, 1000):
    sub = '10'* i
    if sub in s:
        print(i, sub)