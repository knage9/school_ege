import itertools

for x in itertools.product([True, False], repeat = 2):
    A, B = x[0], x[1]
    print(A, B, (not(A and B) and (B or A)))