
for s in range(1, 67+1):
    piles = [16, s]
    piles_sews = [[16+1, s], [16, s+1], [16*2, s], [16, s*3]]
    if sum(piles_sews[0]) >= 84 or sum(piles_sews[1]) >= 84 or sum(piles_sews[2]) >= 84 or sum(piles_sews[3]) >= 84:
        break
    for pile_new in piles_sews:
        b = True
        if sum([pile_new[0]+1, pile_new[1]]) >= 84:
            b = False
        if sum([pile_new[0], pile_new[1]+1]) >= 84:
            b = False
        if sum([pile_new[0]*2, pile_new[1]]) >= 84:
            b = False
        if sum([pile_new[0], pile_new[1]*3]) >= 84:
            b = False
        if sum([(pile_new[0]+1)*2, pile_new[1]]) < 84 and sum([(pile_new[0]+1), pile_new[1]*3]) < 84:
            b = False
        if sum([(pile_new[0]*2), pile_new[1]+1]) < 84 and sum([(pile_new[0]), (pile_new[1]+1)*3]) < 84:
            b = False
        if sum([(pile_new[0]*2)*2, pile_new[1]]) < 84 and sum([(pile_new[0])*2, (pile_new[1]*3)]) < 84:
            b = False
        if sum([(pile_new[0]*2), pile_new[1]*3]) < 84 and sum([(pile_new[0]), (pile_new[1]*3)*3]) < 84:
            b = False
        if b:
            print(s)