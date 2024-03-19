# Case-study #4: Diet meals
# Developers: Solodovnik A., Soknyshev D., Kabanova M., Kim A.
#

import local as ru

cost = 0
protein = 0
leftover = 0

BAR_COST = 99
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


def main_function(meal, prtns, budget):
    match meal:
        case 1:
            if broke(budget, fish(prtns)) == True: print(f'{ru.FOR_MEAL} {ru.OPTION1} {ru.EXPENSES} {fish(prtns)}'
                                          f' {ru.RUBLS}\n {ru.PROSPERITY}\n {ru.BAR}'
                                          f' {int((budget-fish(prtns)) // BAR_COST)}')
            else: print(f'{ru.LACK} {ru.ADD} {round(fish(prtns)-budget, 2)} {ru.RUBLS}')
        case 2:
            if broke(budget, chicken(prtns)): print(f'{ru.FOR_MEAL} {ru.OPTION2} {ru.EXPENSES} {chicken(prtns)}'
                                          f' {ru.RUBLS}\n {ru.PROSPERITY}\n {ru.BAR}'
                                          f' {int((budget-chicken(prtns)) // BAR_COST)}')
            else: print(f'{ru.LACK} {ru.ADD} {round(chicken(prtns)-budget, 2)} {ru.RUBLS}')


if __name__ == "__main__":
    meal = float(input(ru.QUESTION_1))  # local in ()
    prtns = float(input(ru.QUESTION_2))  # local in ()
    budget = float(input(ru.QUESTION_3))  # local in ()
    main_function(meal, prtns, budget)
