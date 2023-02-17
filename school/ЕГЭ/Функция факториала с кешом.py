# cache = dict()
#
# def f(n):
#     if n in cache:
#         print("Ура!! Используем кэш!")
#         return cache[n]
#     if n == 1:
#         res = 1
#         cache[n] = res
#         return 1
#     res = f(n - 1) * n
#     cache[n] = res
#     return res

from functools import lru_cache

# bla

@lru_cache(None)
def f(n):
    if n == 1:
        return 1
    return f(n - 1) * n

for i in range(1, 20):
    f(i)


print(f(5))