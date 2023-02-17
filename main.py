import itertools

s = "AEBCDF"
count = 0
for el in itertools.product(s, repeat=6):
    print(el)
    break
print(count)