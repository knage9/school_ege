from collections import Counter


a = open("for_9.txt").read().replace("	", ".").splitlines()

res = 0
for i in range(len(a)):
    b = a[i].split(".")
    b = list(map(int, b))
    matrix = set(b)
    if len(matrix) == 5:
        x = Counter(b).most_common()[0][0]
        matrix = list(matrix)
        del_el = matrix.index(x)
        del matrix[del_el]
        if (sum(matrix)/len(matrix)) <= ((Counter(b).most_common()[0][0]) * 2):
            print(matrix, Counter(b).most_common()[0])
            res += 1
print(res)