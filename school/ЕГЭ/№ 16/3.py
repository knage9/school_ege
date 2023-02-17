def g(n):
    if n <= 1:
        return 0
    if n > 1:
        return f(n-1)+n

def f(x):
    if x <= 2:
        return 0
    if x > 2:
        return g(x-2)
print(f(8))