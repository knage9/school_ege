s = open("24 (4).txt").readline()

s = s.replace('A', '1').replace('E', '1').replace('U', '1').replace('B', '0').replace('C', '0').replace('D', '0').replace('F', '0')
for i in range(1, 1000):
    sub = '010'* i
    if sub in s:
        print(i, sub)