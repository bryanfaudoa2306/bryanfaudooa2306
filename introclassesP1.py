'''
create a simple class
atributes - variables
methods - functions working usually with atributes
'''
class CashRegister:
    global rate
    rate = .078  # here should be the global variables. Global vars are accessible throughout the whole class

    def __init__(self):
        self.items = 0
        self.price = 0

    #methods
    def update_register(self,price):
        self.items += 1
        self.price+= price
    def display_register(self):
        return print('number of items =', self.items, '\n total price =', self.price)

    def clean_register(self):
        CashRegister.final_price_tax(self)
        self.items = 0
        self.price = 0

    def final_price_tax(self):
        self.price = (1 + rate)*self.price
        return print('final price, taxes included',round(self.price, 2))


register1 = CashRegister()
register1.update_register(100)
register1.update_register(29.90)
register1.update_register(2.05)
register1.display_register()
# register1.final_price_tax()
register1.clean_register()