import sys

sys.setrecursionlimit(20000)

def d(n):
    if int(n**0.5) == n**0.5:
        return n**0.5
    else:
        return d(n+1)+1

print(int(d(4850)+d(5000)))