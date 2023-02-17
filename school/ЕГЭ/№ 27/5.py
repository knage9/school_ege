with open("adidas.txt") as file:
    data = [list(map(int, i.rstrip().split())) for i in file]

summ = 0
for i in range(len(data)):
    summ += max(data[i])

subtotals_list = list()  # массив промежуточных сумм
for i in range(len(data)):
    subtotal_summ = summ - max(data[i]) + min(data[i])
    if subtotal_summ % 3 != 0:
        subtotals_list.append(subtotal_summ)

print(max(subtotals_list))