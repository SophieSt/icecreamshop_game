from random import randint

from utils.print_statements_icecream import print_finance_overview, print_icecream
from ice_cream_shop import ice_cream_shop

# CONE YOU DO IT
# Imagine you're an ice cream shop owner!
# Your goal is to make as much money money as possible.
# Every day you will be given the weather forecast (expected temperature).
# Based on that you decide:
# 1) amount of ice cream you buy
# 2) number of cones you buy
# 3) price per ice cream
#
# At the end of the day you will be given:
# 1) actual amount of sold cream
# 2) the impact on your assets (budget, ice cream, and cones).
#
# If you're not broke at the end of the day, you can again.


def game():

    # welcome to the show
    print("Welcome to CONE YOU DO IT: Your ice cream shop.\n")

    # initiate game
    still_gaming = True
    play_round = 1
    cost_operating = 75
    cost_icecream = 0.3
    cost_cone = 0.15

    shop = ice_cream_shop()    

    # start the game
    while still_gaming:
        # randomly generate weather
        pred_temperature = randint(-10, 40)

        # Tell player day's stats
        print(f"The weather today is {pred_temperature} degrees celsius.")
        shop.print_balance()

        # let user stock up on ice cream
        shop.buy_ice_cream(cost_icecream)

        # let user stock up on cones
        shop.buy_cones(cost_cone)

        # let user decide on price per ice cream
        shop.set_price()

        # calculate day results
        shop.get_sales(temperature=pred_temperature)
        (old_balance, expenses_icecream, expenses_cones, income, new_balance) = shop.get_financial_day_results(
            cost_cone=cost_cone,
            cost_ice_cream=cost_icecream,
            cost_operating=cost_operating)

        # return results to the player
        print_finance_overview(
            balance=old_balance,
            cost_operating=cost_operating,
            expenses_icecream=expenses_icecream,
            expenses_cones=expenses_cones,
            income=income,
            new_balance=new_balance,
            play_round=play_round)

        shop.end_day()
        # if new balance still < 75, player is broke and game ends
        if not shop.is_solvent:
            still_gaming = False

        # ask player to play another round
        new_round = input("Let's play another round!  (Y/N)\n")
        if (new_round == "Y") or (new_round == "y"):
            play_round += 1
        else:
            still_gaming = False

    print_icecream()


# Let's play!
game()
