# Case-study #4: Diet meals
# Developers: Solodovnik A., Soknyshev D., Kabanova M., Kim A.
#

import local as ru

cost = 0
protein = 0
leftover = 0

PROTEIN_COST = 99
FISH_COST = 314.15
CHICKEN_COST = 499.29


def fish(x):
    cost = FISH_COST * x
    return cost

def chicken(x):
    cost = CHICKEN_COST * x
    return cost

def broke(x, y):
    leftover = x - y
    return leftover > 0

meal = int(input(ru.QUESTION_1)) # local in ()
portions = int(input(ru.QUESTION_2)) # local in ()
budget = int(input(ru.QUESTION_3)) # local in ()
match meal:
    case 1:
        if broke(budget,cost) == True: print(f'{ru.EXPENSES} {meal} {ru.RUBLS}\n {ru.PROSPERITY}\n {ru.BAR}'
              f' {(broke(budget,cost))//PROTEIN_COST}')
        else

