
#Задача на одну кучу
# https://inf-ege.sdamgia.ru/problem?id=27802
# for s in range(1, 67):
#     s_news = [s+1, s+4, s*5]
#     if s_news[0] > 68 or s_news[1] > 68 or s_news[2] > 68:
#          break
#     for s_new in s_news:
#         b = False
#         if ((s_new + 1 >= 68) or (s_new + 4 >= 68) or (s_new * 5 >= 68)) and(s_new<=68):
#             b = True
#         if b:
#             print(s)

#Задача на две кучи
#https://inf-ege.sdamgia.ru/problem?id=27417
for s in range(1, 69+1):
    piles = [7, s]
    piles_sews = [[7+1, s], [7, s+1], [7*2, s], [7, s*2]]
    if sum(piles_sews[0]) >= 77 or sum(piles_sews[1]) >= 77 or sum(piles_sews[2]) >= 77:
        break
    for pile_new in piles_sews:
        b = True
        if sum([pile_new[0]+1, pile_new[1]]) >= 77:
            b = False
        if sum([pile_new[0], pile_new[1]+1]) >= 77:
            b = False
        if sum([pile_new[0]*2, pile_new[1]]) >= 77:
            b = False
        if sum([pile_new[0], pile_new[1]*2]) >= 77:
            b = False
        if sum([(pile_new[0]+1)*2, pile_new[1]]) and sum([(pile_new[0]+1), pile_new[1]*2]) < 77:
            b = False
        if sum([(pile_new[0]*2), pile_new[1]+1]) and sum([(pile_new[0]), (pile_new[1]+1)*2]) < 77:
            b = False
        if sum([(pile_new[0]*2)*2, pile_new[1]]) and sum([(pile_new[0])*2, (pile_new[1]*2)]) < 77:
            b = False
        if sum([(pile_new[0]*2), pile_new[1]*2]) and sum([(pile_new[0]), (pile_new[1]*2)*2]) < 77:
            b = False
        if b:
            print(s)