sequence = [823, 707, 71, 570, 666, 232, 702, 886, 636, 287, 88, 214, 827, 876, 18, 704, 227, 89, 595, 411]
count_divisible_by_2 = 0
count_divisible_by_13 = 0
count_divisible_by_26 = 0

for num in sequence:
    if num % 2 == 0 and num % 13 != 0:
        count_divisible_by_2 += 1
    elif num % 13 == 0 and num % 2 != 0:
        count_divisible_by_13 += 1
    elif num % 26 == 0:
        count_divisible_by_26 += 1

count_pairs_2_13 = count_divisible_by_2 * count_divisible_by_13
count_pairs_26 = count_divisible_by_26
count_pairs = count_pairs_2_13 + count_pairs_26