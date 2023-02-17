for n in range(100):
    for m in range(100):
        N = 2**m * 3**n
        if n % 2 != 0 and m % 2 == 0 and 400_000_000 <= N <= 600_000_000:
            print(N)