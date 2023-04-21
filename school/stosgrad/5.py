N = 123_458
N_2 = bin(N)[2::]
b = str(N).replace("3", "1").replace("5", "1").replace("7", "1").replace("9", "1").replace("2", "2").replace("4", "2")\
.replace("6", "2").replace("8", "2").replace("10", "2")
cal_1 = b.count("1")
cal_2 = b.count("2")
if cal_2 > cal_1:
    N_2 = str(N_2) + "1"
elif cal_1 > cal_2:
    N_2 = str(N_2) + "0"
elif cal_1 == cal_2 and N % 2 == 0:
    N_2 = str(N_2) + "0"
elif cal_1 == cal_2 and N % 2 != 0 :
    N_2 = str(N_2) + "1"
N = int(N_2, 2)
N_2 = bin(N)[2::]
b = str(N).replace("3", "1").replace("5", "1").replace("7", "1").replace("9", "1").replace("2", "2").replace("4", "2")\
.replace("6", "2").replace("8", "2").replace("10", "2")
cal_1 = b.count("1")
cal_2 = b.count("2")
if cal_2 > cal_1:
    N_2 = str(N_2) + "1"
elif cal_1 > cal_2:
    N_2 = str(N_2) + "0"
elif cal_1 == cal_2 and N % 2 == 0:
    N_2 = str(N_2) + "0"
elif cal_1 == cal_2 and N % 2 != 0 :
    N_2 = str(N_2) + "1"
N = int(N_2, 2)
N_2 = bin(N)[2::]
b = str(N).replace("3", "1").replace("5", "1").replace("7", "1").replace("9", "1").replace("2", "2").replace("4", "2")\
.replace("6", "2").replace("8", "2").replace("10", "2")
cal_1 = b.count("1")
cal_2 = b.count("2")
if cal_2 > cal_1:
    N_2 = str(N_2) + "1"
elif cal_1 > cal_2:
    N_2 = str(N_2) + "0"
elif cal_1 == cal_2 and N % 2 == 0:
    N_2 = str(N_2) + "0"
elif cal_1 == cal_2 and N % 2 != 0 :
    N_2 = str(N_2) + "1"
print(int(N_2, 2))