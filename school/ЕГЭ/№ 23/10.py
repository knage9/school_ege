

# count = 0
# def f(x, y, last1=False, last2=False):
#     global count
#     b = False
#     if last1 != last2:
#         b = True
#     if x == y and b:
#         count += 1
#     if x == 11:
#         last1 = True
#     if x == 12:
#         last2 = True
#     if x <= y:
#         f(x + 1, y, last1, last2)
#         f(x * 2, y, last1, last2)
# f(2, 24)
# print(count)

def f(x, t, arr=[""]):
    if x == t:
        arr = arr + [str(x)]
        if "12" in arr or "11" in arr:
            if not("12" in arr and "11" in arr):
                print(" ".join(arr))
    if x <= t:
        f(x + 1, t, arr + [str(x)])
        f(x * 2, t, arr + [str(x)])
f(2, 24)