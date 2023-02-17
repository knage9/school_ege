s = open("1.txt").readline()

s = s.replace('B', 'A').replace('2', '1')
for i in range(1, 1000):
    sub = '11A'* i
    if sub in s:
        print(i, sub)