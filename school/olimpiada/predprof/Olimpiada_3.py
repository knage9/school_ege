nums = 112


def f(nums, c, count=0):
    if c == 17: return 1
    if nums < 0 or int(nums ** 0.5) != nums ** 0.5: return f(nums - 2, c + 1) + f(nums - 3, c + 1)
    return f(nums - 2, c + 1) + f(nums - 3, c + 1) + f(int(nums ** 0.5), c + 1)


print(f(112, 0))