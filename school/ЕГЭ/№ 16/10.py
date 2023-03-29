from functools import lru_cache


@lru_cache(None)
def G(n):
    if n <= 2:
        return 1
    if n > 2 and n % 2 == 0:
        return f(n - 3) + f(n - 2)
    else:
        return f(n + 1) - G(n - 1)


@lru_cache(None)
def f(n):
    if n < 3:
        return 1
    if n > 2 and n % 2 == 0:
        return G(n) + f(n - 1)
    else:
        return f(n - 2) - 2 * G(n + 1)



print(G(120))