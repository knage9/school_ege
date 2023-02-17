from functools import lru_cache

@lru_cache(None)
def f(n):
    if n <= 2:
        return 1
    if n > 2:
        return n*f(n-2)

for i in range(1, 3000):
    f(i)
print(f(3000)//f(2996))