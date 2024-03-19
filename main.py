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


def main_function(meal, budget):
    match meal:
        case 1:
            if broke(budget, cost): print(f'{ru.EXPENSES} {ru.OPTION1} {ru.RUBLS}\n {ru.PROSPERITY}\n {ru.BAR}'
                      f'{(broke(budget, cost)) // PROTEIN_COST}')
            else: print(f'{ru.LACK} {ru.ADD} {cost-budget} {ru.RUBLS}')
        case 2:
            if broke(budget, cost):  print(f'{ru.EXPENSES} {ru.OPTION2} {ru.RUBLS}\n {ru.PROSPERITY}\n {ru.BAR}'
                      f'{(broke(budget, cost)) // PROTEIN_COST}')
            else: print(f'{ru.LACK} {ru.ADD} {cost - budget} {ru.RUBLS}')
        case _:
            print(f'{ru.ERROR}')


if __name__ == "__main__":
    meal = int(input(ru.QUESTION_1))  # local in ()
    portions = int(input(ru.QUESTION_2))  # local in ()
    budget = int(input(ru.QUESTION_3))  # local in ()
    main_function(meal, budget)
