class ATM():
    def __init__(self,withdraw,deposit,balance,bankStatement):
        self.withdraw=withdraw
        self.deposit=deposit
        self.balance=balance
        self.bankStatement=bankStatement
    def MoneyWithdrawal(self):
        print('Money Has Been Withdrawn')

    def MoneyDeposit(self):
        print('Money Has Been Deposited')
    
IDFC=ATM(10000,5000,15000,10000)
print(IDFC.deposit)
print(IDFC.MoneyWithdrawal())