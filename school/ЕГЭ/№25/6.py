
for n in range(29):
    for m in range(29):
        N = 2**m * 3**n
        if m % 2 == 0 and n % 2 != 0 and 200_000_000 <= N <= 400_000_000:
            print(N)