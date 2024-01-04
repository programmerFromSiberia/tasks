class User:
    def __init__(self, name, surname, postal_code):
        self.name = name
        self.surname = surname
        self.postal_code = postal_code
        self.accounts = []  # список открытых счетов для пользователя

    def add_account(self, currency):
        account = Account(currency)
        self.accounts.append(account)

    def view_accounts(self):
        if len(self.accounts) == 0:
            print("У пользователя нет открытых счетов.")
        else:
            for account in self.accounts:
                print(f"Валюта: {account.currency}")


class Account:
    def __init__(self, currency):
        self.currency = currency


def main():
    users = []

    while True:
        print("\n======= Банк =======")
        print("1. Добавить пользователя")
        print("2. Открыть счет для пользователя")
        print("3. Просмотреть учетные записи пользователя")
        print("0. Выход")
        choice = int(input("Выберите действие: "))

        if choice == 0:
            break
        elif choice == 1:
            name = input("Введите имя пользователя: ")
            surname = input("Введите фамилию пользователя: ")
            postal_code = input("Введите почтовый код пользователя: ")

            user = User(name, surname, postal_code)
            users.append(user)
            print("Пользователь успешно добавлен.")
        elif choice == 2:
            if not users:
                print("Необходимо сначала добавить пользователя.")
                continue

            print("Выберите пользователя из списка:")
            for i, user in enumerate(users):
                print(f"{i + 1}. {user.name} {user.surname}")

            user_choice = int(input("Введите номер пользователя: ")) - 1

            valid_currencies = ["Dollar", "Pound", "Rupee"]
            print("Выберите валюту счета:")
            for i, currency in enumerate(valid_currencies):
                print(f"{i + 1}. {currency}")

            currency_choice = int(input("Введите номер валюты: ")) - 1

            users[user_choice].add_account(valid_currencies[currency_choice])
            print("Счет успешно открыт для пользователя.")
        elif choice == 3:
            if not users:
                print("Нет зарегистрированных пользователей.")
                continue

            print("Выберите пользователя из списка:")
            for i, user in enumerate(users):
                print(f"{i + 1}. {user.name} {user.surname}")

            user_choice = int(input("Введите номер пользователя: ")) - 1

            print("\nУчетные записи пользователя:")
            users[user_choice].view_accounts()
        else:
            print("Неверный выбор. Попробуйте еще раз.")


if __name__ == '__main__':
    main()
