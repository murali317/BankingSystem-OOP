class User:
    # name, user_id, account_list
    def __init__(self, name, user_id, account_lst):
        self.name = name
        self.user_id = user_id
        self.account_lst = account_lst
    def view_accounts(self):
        for account in self.account_lst:
            print(account, end=' ')

class Account:
    def __init__(self, acc_number, acc_type, balance):
        self.acc_number = acc_number
        self.acc_type = acc_type
        self.balance = balance
    def deposit(self, amount):
        # amount = int(input('Enter amount to deposit')) # makes testing hard
        if amount >= 10:
            self.balance += amount
            print(f'{amount} is deposited successfully.')
        else:
            print('Minimum amount to deposit is 10rs')
    def withdrawal(self, amount):
        if 200 <= amount <= self.balance:
            self.balance -= amount
            print(f'{amount} is withdrawn successfully')
        elif amount > self.balance:
            print('Insufficient balance to withdraw')
        else:
            print('Minimum amount to withdraw is 200')
    def balance_check(self):
        print(f'Your account balance is {self.balance}')
    def __str__(self):
        return f'Account number #{self.acc_number} | Type: {self.acc_type} | Balance: ₹{self.balance}'

class Savings_account(Account):
    def __init__(self, acc_number, balance, interest_rate):
        super().__init__(acc_number, 'Savings', balance)
        self.interest_rate = interest_rate
    def apply_interest(self):
        self.balance += self.balance * self.interest_rate
        print(f'Your new balance after adding interest is {self.balance}')

class Bank:
    def __init__(self):
        self.users = {}
        self.userid_counter = 100
    def create_user(self, name):
        user_id = self.userid_counter
        self.userid_counter += 1 # incrementing for next users
        newUser = User(name, user_id, [])
        self.users[user_id] = newUser
        print(f'User {name} with ID {user_id} has been created')
    def create_account(self, user_id, acc_type, balance):
        if user_id not in self.users:
            print('❌ User not found!')
            return
        acc_num = 1000 + len(self.users[user_id].account_lst)
        if acc_type == 'Savings':
            account = Savings_account(acc_num, balance, interest_rate = 0.07)
        else:
            account = Account(acc_num, acc_type, balance)
        self.users[user_id].account_lst.append(account) # Append the account object to later call .deposit()/.withdraw()...
        print(f'A {acc_type} Account has been created for user_id: {user_id} with balance {balance}')
    def show_all_users(self):
        pass
    def get_user_accounts(self, user_id):
        pass

b = Bank()
b.create_user('Krishna')
b.create_account(100, 'Savings', 1000)
b.users[100].account_lst[0].balance_check() # will fetch the balance
acc1 = Account(acc_number=1000, acc_type='Current', balance=5000)
u = User('Krishna', 100, [acc1])
u.view_accounts()

# bank = Account(acc_number=101, acc_type='Current', balance=1000)
# bank.withdrawal(amount=int(input('Enter an amount to withdraw')))
# acc = Savings_account(acc_number=102, balance=500, interest_rate=0.08)
# acc.apply_interest()
