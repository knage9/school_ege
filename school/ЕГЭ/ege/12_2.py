for k1 in range(60):
    for k2 in range(60):
        for k3 in range(60):
            s = '0' + '1' * k1 + '2' * k2 + '3' * k3
            while '01' in s or '02' in s or '03' in s:
                s = s.replace('01', '30')
                s = s.replace('02', '101')
                s = s.replace('03', '202')
            if s.count('1') == 15 and s.count('2') == 10 and s.count('3') == 60:
                print(k1)