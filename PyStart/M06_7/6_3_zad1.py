class BankAccount:

    def __init__(self):
        self._amount = 0

    def deposit(self, amount: int):  # wplacanie
        self._amount += amount

    def withdraw(self, amount: int):
        if amount > self._amount:
            to_withdraw = self._amount
            self._amount = 0
            return to_withdraw
        self._amount -= amount
        return amount

class SavingsAccount(BankAccount):

    def __init__(self, percent: float):
        super().__init__()
        self.percent = percent

    def accumulate(self):
        self._amount += self._amount * self.percent


def test_savings_account():
    # given
    account = SavingsAccount(0.1)
    account.deposit(1000)

    # when
    account.accumulate()

    # then
    assert account.withdraw(1100) == 1100
    assert account.withdraw(1100) == 0
