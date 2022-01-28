class BankCard:
    def __init__(self, owner, number, provider):
        self.owner = owner
        self.number = number
        self.provider = provider
    def get_number(self):
        print("Getting number...")
    def get_owner(self):
        print("Getting owner...")
    def get_provider(self):
        print('Getting provider...')
class BankAccount:
    def __init__(self, owner, balance,bank):
        self.owner=owner
        self.balance=balance
        self.bank=bank
    def get_owner(self):
        print("Getting owner...")
    def get_balance(self):
        print('Getting balance...')
    def get_bank(self):
        print('Getting bank...')
    def set_balance(self):
        print("Setting balance...")
class Bank:
    def __init__(self, name,bank_accounts, bank_cards):
        self.name=name
        self.bank_accounts=bank_accounts
        self.bank_cards=bank_cards
    def get_bank_accounts(self):
        print("Getting bank accounts...")
    def get_bank_cards(self):
        print('Getting bank cards...')
class CreditCard(BankCard):
    def __init__(self, owner, number, provider, balance, payments_history):
        super().__init__(owner, number, provider)
        self.balance=balance
        self.payments_history=payments_history
    def balance(self):
        print("Balancing...")
    def payments_history(self):
        print('Payments history')
class GoldenCreditCard(CreditCard):
    def __init__(self, owner, number, provider, balance, payments_history, financial_manager):
        super().__init__(owner, number, provider, balance, payments_history)
        self.financial_manager=financial_manager
    def get_financial_manager(self):
        print('Getting financial manager...')
    def set_financial_manager(self):
        print('Setting financial manager')
class PremiumBankAccount(BankAccount):
    def __init__(self, owner, balance, bank, financial_manager):
        super().__init__(owner, balance, bank)
        self.financial_manager=financial_manager
    def get_financial_manager(self):
        print('Getting financial manager...')
    def set_financial_manager(self):
        print('Setting financial manager...')

class StudentBankAccount(BankAccount):
    def __init__(self, owner, balance, bank, overdraft_balance, overdraft_limit):
        super().__init__(owner, balance, bank)
        self.overdraft_balance = overdraft_balance
        self.overdraft_limit = overdraft_limit
    def get_overdraft_balance(self):
        print('Getting overdraft balance...')
    def set_overdraft_balance(self):
        print('Setting overdraft balance.')
    def get_overdraft_limit(self):
        print('Getting overdraft limit...')
    def set_overdraft_limit(self):
        print('Setting overdraft limit...')



karta1=BankCard('Adrian Urbanek', '1234', "Bank Warszawski")
print('Sprawdzenie danych karty...')
karta1.get_owner()
karta1.get_number()
karta1.get_provider()

StudentBankAccount1=StudentBankAccount('Adrian Urbanek', '1000','Millenium', '100', '200')
StudentBankAccount1.get_overdraft_balance()

PremiumBankAccount1=PremiumBankAccount('Adrian','1000', 'Bank', 'Manager finansow')
PremiumBankAccount1.get_financial_manager()


def get_overdraft_balance(self):
    print('Getting overdraft balance...')


def set_overdraft_balance(self):
    print('Setting overdraft balance.')


def get_overdraft_limit(self):
    print('Getting overdraft limit...')


def set_overdraft_limit(self):
    print('Setting overdraft limit...')






