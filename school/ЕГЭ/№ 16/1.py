def func(x):
    if x == 1:
        return 1
    if x%2 == 0:
        return (x+func(x-1))
    if x>1 and x%2 != 0:
        return(3*func(x-2))
print(func(25))