class Bank:
    def __init__(self):
        pass

    def create(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, balance):
        self.balance += balance

    def withdraw(self, balance):
        if (self.balance - balance) >= 0:
            self.balance -= balance
        else:
            raise notenoughbal

    def get_balance(self):
        return self.balance


class accnotfound(Exception):
    pass


class notenoughbal(Exception):
    pass


users = {}
while True:
    data = input().strip().split()
    try:
        op, name, balance = data
        balance = int(balance)
    except ValueError:
        op = data[0] if len(data) > 0 else ""
        name = data[1] if len(data) > 1 else ""
        if len(data) > 2:
            balance = data[2]
            balance = int(balance)
        else:
            balance = 0

        if op == "stop":
            break
    try:
        if op != "" and op != "create" and (name not in users):
            raise accnotfound

        if op == "create":
            # print("creat")
            obj = Bank()
            obj.create(name, balance)
            users[name] = obj
        elif op == "deposit":
            # print("deposit")
            users[name].deposit(balance)
        elif op == "withdraw":
            # print("withdraw")
            users[name].withdraw(balance)
        elif op == "balance":
            print(users[name].get_balance())
        else:
            pass
    except accnotfound:
        print("Account not found")
    except notenoughbal:
        print("Insufficient funds")
