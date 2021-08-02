class atm(object):
    def _init_(self,atmCardNumber,AtmPinNumber):
        self.atmCardNumber=atmCardNumber
        self.AtmPinNumber=AtmPinNumber


    def CashWithdraw(self,cash):
        cash=input('Type in the amount of money... ')
        print(cash, "Your withdraw has been successful, have a great day.")

lol=atm(7)
print(lol.atmCardNumber)
print(lol.AtmPinNumber)
lol.CashWithdraw(500)