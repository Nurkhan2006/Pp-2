class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Пополнено: {amount}. Новый баланс: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Недостаточно средств!")
        else:
            self.balance -= amount
            print(f"Снято: {amount}. Остаток: {self.balance}")

acc = Account("Иван", 100)
acc.deposit(50)  
acc.withdraw(30)  
acc.withdraw(200)  
