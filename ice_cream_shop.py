class ice_cream_shop(object):
    def __init__(self):
        self.balance = 1000.00
        self.stock_cones = 0
        self.stock_ice_cream = 0
        self.ice_cream_selling_price = 0.00
        self.is_solvent = True
        self.ice_cream_sold = 0
        self.bought_cones = 0
        self.bought_ice_cream = 0
        self.new_balance = 1000.00

    def print_balance(self):
        print(
            f"Your current balance is € {self.balance} and you have {self.stock_cones} cone(s) in stock.\n")

    def buy_ice_cream(self, cost_ice_cream):
        ''' Ask the user for amount of ice cream they want to purchase.
        Check if input is valid.
        '''
        new_ice_cream = input(
            f"Stock up your ice cream (€ {cost_ice_cream}), don't forget to keep some money for the cones (max: 2055):\n")
        try:
            new_ice_cream = int(new_ice_cream)
            if (new_ice_cream >= 2055) or (new_ice_cream < 0):
                raise Exception("Please enter an integer between 0 and 2055!")
            if ((new_ice_cream * cost_ice_cream) > self.new_balance):
                max_affordable = self.new_balance / cost_ice_cream
                raise Exception(f"Oops! You can only afford {max_affordable} ice_cream(s).")
        except Exception as e:
            print(e.args)
            self.buy_ice_cream(cost_ice_cream)

        # change balance & stock
        self.new_balance -= new_ice_cream * cost_ice_cream
        self.stock_ice_cream = new_ice_cream
        self.bought_ice_cream = new_ice_cream

    def buy_cones(self, cost_cone):
        ''' Ask the user for amount of cones they want to purchase.
        Check if input is valid.
        '''
        new_cones = input(f"Stock up your cones (€ {cost_cone}, max: 2055):\n")
        try:
            new_cones = int(new_cones)
            if ((new_cones >= 2055) or (new_cones < 0)):
                raise Exception("Please enter an integer between 0 and 2055!")
            if ((new_cones * cost_cone) > self.new_balance):
                max_affordable = self.new_balance / cost_cone
                raise Exception(f"Oops! You can only afford {max_affordable} cone(s).")
        except Exception as e:
            print(e.args)
            self.buy_cones(cost_cone)

        # change balance & stock
        self.new_balance -= new_cones * cost_cone
        self.stock_cones += new_cones
        self.bought_cones = new_cones

    def set_price(self):
        ''' Ask the user for the selling price per ice cream.
        Check if input is valid.
        '''
        price_icecream = input(
            "Set your selling price for your delicious ice creams € x.xx:\n")
        try:
            price_icecream = float(price_icecream)
            if (price_icecream < 0):
                raise ValueError
        except ValueError:
            print("Please enter a float > 0!")
            price_icecream = self.set_price()

        self.ice_cream_selling_price = price_icecream


    def get_sales(self, temperature):
        ''' Calculate how much ice cream the shop owner sold.
        On warm days, this is more.
        On cold days less.
        '''
        # get maximum sales of ice cream per day given temperature and price per ice cream
        max_ice_cream_sales_per_day = self.get_max_ice_cream_sales_per_day(temperature)

        # get actual sales of ice cream per day given max_sales, stock of ice cream, and stock of cones
        actual_sales = self.get_actual_sales_per_day(
            max_ice_cream_sales_per_day)

        self.ice_cream_sold = actual_sales
        print(f"You sold {actual_sales} ice cream(s).\n")


    def get_actual_sales_per_day(self, max_sales_per_day):
        ''' Calculate amount of actual sales per day.
        Can only be as much as potantially possible and available.
        '''
        actual_sales = min(max_sales_per_day, self.stock_ice_cream, self.stock_cones)
        return actual_sales

    def get_max_ice_cream_sales_per_day(self, temperature):
        ''' Calculate potential ice cream sales per day based on temperature and price.
        Cannot be negative.
        '''
        max_sales = 1000 * temperature * (10 - self.ice_cream_selling_price)

        if (max_sales < 0):
            max_sales = 0

        return max_sales

    def get_financial_day_results(self, cost_cone, cost_ice_cream, cost_operating):
        ''' calculate expenses, income, and new balance after a day in the life of the ice crean shop owner.
        '''

        # calculate expenses
        expenses_icecream = self.bought_ice_cream * cost_ice_cream
        expenses_cones = self.bought_cones * cost_cone

        # calculate income
        income = self.ice_cream_sold * self.ice_cream_selling_price

        # calculate new balance
        self.new_balance = self.balance - cost_operating - \
            expenses_icecream - expenses_cones + income

        return (self.balance, expenses_icecream, expenses_cones, income, self.new_balance)

    def end_day(self):
        self.balance = self.new_balance
        self.is_solvent = (self.balance > 75)
        self.stock_ice_cream = 0
        self.stock_cones -= self.ice_cream_sold       
        if not self.is_solvent:
            print("Sorry, you're bankrupt. More luck next time!\n")
