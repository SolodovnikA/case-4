# Case-study #4: Diet meals
# Developers: Solodovnik A., Soknyshev D., Kabanova M., Kim A.
#

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

def broke(x):
    leftover = budget - cost
    return leftover > 0

serving = int(input()) # local in ()
budget = int(input()) # local in ()
meal = int(input()) # local in ()
match meal:
    case 1:
        print(f'{8594}')

