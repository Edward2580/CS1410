class Bank_Account:

    def __init__(self, name, account_number):
        self._name = name
        self._account_number = account_number
        self._balance = 0.0

    def deposit(self, amount):
        self._balance = self._balance + amount

    def withdraw(self, amount):
        self._balance = self._balance - amount

    def get_balance(self):
        return self._balance

    def get_name(self):
        return self._name

    def get_account_num(self):
        return self._account_number
