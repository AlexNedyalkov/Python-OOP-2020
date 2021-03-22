from polymorphism_06.exercises.account_03 import Account

import unittest

class TestAccount(unittest.TestCase):

    def setUp(self):
        self.account = Account('Baicho', 100)

    def test_account_init(self):
        self.assertEqual(self.account.owner, 'Baicho')
        self.assertEqual(self.account.amount, 100)

    def test_account_starts_with_zero(self):
        self.new_account = Account('Pesho')
        self.assertEqual(self.new_account.amount, 0)

    def test_add_proper_transaction(self):
        self.account.add_transaction(10)
        self.assertEqual(self.account._transactions[0], 10)

    def test_validate_account(self):
        self.account.validate_transaction(self, 100)
        self.assertEqual(self.account.balance, 110)

    def test_add_transaction_non_int(self):
        self.assertRaises(ValueError, self.account.add_transaction, 'baicho')

    def test_account_balance(self):
        self.account.add_transaction(10)
        self.account.add_transaction(5)
        self.assertEqual(self.account.balance, 115)

    def test_account_len(self):
        self.account.add_transaction(10)
        self.account.add_transaction(5)
        self.assertEqual(len(self.account), 2)

    def test_account_str(self):
        self.assertEqual(f'Account of {self.account.owner} with starting amount: {self.account.amount}',str(self.account))
    
    def test_account_repr(self):
        self.assertEqual(f'Account({self.account.owner}, {self.account.amount})', repr(self.account))

    def test_account_reversed(self):
        self.account.add_transaction(10)
        self.account.add_transaction(5)
        self.assertEqual(list(reversed(self.account)), [5, 10])

    def test_get_item(self):
        self.account.add_transaction(10)
        self.account.add_transaction(5)
        self.assertEqual(self.account[0], 10)
        self.assertEqual(self.account[1], 5)

    def test_validate_transaction(self):
        self.account.add_transaction(-10)

if __name__ == '__main__':
    unittest.main()

