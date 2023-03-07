def func(x):
    if x == 1:
        return 5
    if x == 2:
        return 5
    if x > 2:
        return 5 * func(x-1) - 4*func(x-2)
print(func(13))