from functools import lru_cache

@lru_cache(None)
def f(n):
    if n == 0:
        return 0
    if n % 3 == 2:
        return f(n-1)+1
    if n % 3 < 2:
        return f((n - (n % 3))//3)

for i in range(1, 3000):
    if f(i) == 6:
        print(i)
        break