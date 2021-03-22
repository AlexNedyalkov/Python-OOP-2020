'''
Create a single class called Account. Upon initialization, it should receive owner (str) and amount (int, optional, 0 by default).
It should also have an attribute called _transactions (empty list upon initialization). Create the following methods:
    • add_transaction(amount) – if the amount is not an integer, raise ValueError with message "please use int for amount",
    otherwise, add the amount to the transactions
    • balance() – property that returns sum of the amount and all the transactions
    • validate_transaction(account: Account, amount_to_add) – if the transaction is possible, add it.
     If the balance becomes less than zero, raise ValueError with message "sorry cannot go in debt!" and break the transaction.
     Otherwise, complete it and return a message "New balance: {account_ballance}"
'''
class Account:

    def __init__(self, owner: str, amount: int = 0):
        self.owner = owner
        self.amount = amount
        self._transactions = []

    # @property
    # def owner(self):
    #     return self.__owner
    #
    # @owner.setter
    # def owner(self, new_owner):
    #     self.__owner = new_owner
    #
    # @property
    # def amount(self):
    #     return self.__amount
    #
    # @amount.setter
    # def amount(self, new_amount):
    #     self.__amount = new_amount

    def add_transaction(self, amount: int):
        if isinstance(amount, int):
            self._transactions.append(amount)
        else:
            raise ValueError('please use int for amount')

    @property
    def balance(self):
        return self.amount + sum(self._transactions)

    @staticmethod
    def validate_transaction(account, amount_to_add):
        if account.balance >= amount_to_add:
                account.add_transaction(amount_to_add)
                return f"New balance: {account.balance}"
        else:
            raise ValueError('Sorry cannot go in debt')

    def __str__(self):
        return f'Account of {self.owner} with starting amount: {self.amount}'

    def __repr__(self):
        return f'Account({self.owner}, {self.amount})'

    def __len__(self):
        return len(self._transactions)

    def __reversed__(self):
        return reversed(self._transactions)

    def __getitem__(self, item):
        return self._transactions[item]

    def __gt__(self, other):
        return self.balance > other.balance

    def __ge__(self, other):
        return self.balance >= other.balance

    def __lt__(self, other):
        return not self.__ge__(other)

    def __le__(self, other):
        return not self.__gt__(other)

    def __eq__(self, other):
        return self.balance == other.balance

    def __ne__(self, other):
        return not self.__eq__(other)

    def __add__(self, other):
        new_account =  Account(f'{self.owner}&{other.owner}', self.amount + other.amount)
        new_account._transactions.extend(self._transactions + other._transactions)

        return new_account

if __name__ == '__main__':

    acc = Account('bob', 10)
    acc2 = Account('john')
    print(acc)
    print(repr(acc))
    acc.add_transaction(20)
    acc.add_transaction(-20)
    acc.add_transaction(30)
    print(acc.balance)
    print(len(acc))
    for transaction in acc:
        print(transaction)
    print(acc[1])
    print(list(reversed(acc)))
    acc2.add_transaction(10)
    acc2.add_transaction(60)
    print(acc > acc2)
    print(acc >= acc2)
    print(acc < acc2)
    print(acc <= acc2)
    print(acc == acc2)
    print(acc != acc2)
    acc3 = acc + acc2
    print(acc3)
    print(acc3._transactions)
