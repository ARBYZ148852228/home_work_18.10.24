class BankAccount:
    def __init__(self, balance):  # Исправлено на двойное подчеркивание
        self.__balance = balance  # Приватная переменная

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount  # Исправлено на двойное подчеркивание

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:  # Исправлено на двойное подчеркивание
            self.__balance -= amount  # Исправлено на двойное подчеркивание
        else:
            print("Недостаточно средств")

    def get_balance(self):
        return self.__balance  # Исправлено на двойное подчеркивание


# Пример использования
account = BankAccount(1000)
account.deposit(500)
print(account.get_balance())  # 1500

# account.__balance  # Это вызовет ошибку, так как __balance приватная
