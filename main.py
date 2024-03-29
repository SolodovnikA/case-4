# Case-study #4: Diet meals
# Developers: Solodovnik A., Soknyshev D., Kabanova M., Kim A.
#

import local as ru

BAR_COST = 99
FISH_COST = 314.15
CHICKEN_COST = 499.29

cost = 0
leftover = 0
result = 0


def fish(x):
    """"
    A function that calculates the final price of the meal.
    """
    cost = FISH_COST * x
    return cost


def chicken(x):
    cost = CHICKEN_COST * x
    return cost


def broke(x, y):
    """
    This function calculates the balance of a purchase.
    """
    leftover = x - y
    return leftover > 0


def main_function(meal, prtns, budget):
    """
    Final calculation.
    """
    match meal:
        case 1:
            if broke(budget, fish(prtns)): result = (f'{ru.FOR_MEAL} {ru.OPTION1} {ru.EXPENSES} {fish(prtns)} '
                                                     f'{ru.RUBLS}\n {ru.PROSPERITY}\n {ru.BAR}'
                                                     f'{int((budget-fish(prtns)) // BAR_COST)}')
            else: result = f'{ru.LACK} {ru.ADD} {round(fish(prtns)-budget, 2)} {ru.RUBLS}'
            print(result)
        case 2:
            if broke(budget, chicken(prtns)): result = (f'{ru.FOR_MEAL} {ru.OPTION2} {ru.EXPENSES} {chicken(prtns)} '
                                                        f'{ru.RUBLS}\n {ru.PROSPERITY}\n {ru.BAR}'
                                                        f' {int((budget-chicken(prtns)) // BAR_COST)}')
            else: result = f'{ru.LACK} {ru.ADD} {round(chicken(prtns)-budget, 2)} {ru.RUBLS}'
            print(result)
        case _:
            print(ru.ERROR)



if __name__ == "__main__":
    meal = float(input(ru.QUESTION_1))
    prtns = float(input(ru.QUESTION_2))
    budget = float(input(ru.QUESTION_3))
    main_function(meal, prtns, budget)
