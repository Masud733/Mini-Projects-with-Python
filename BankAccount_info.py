class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount}. New balance: ${self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("Insufficient funds.")

    def display_balance(self):
        print(f"Account {self.account_number} balance: ${self.balance}")


def main():
    account_number = input("Enter account number: ")
    initial_balance = float(input("Enter initial balance: "))
    account = BankAccount(account_number, initial_balance)

    while True:
        print("\n1. Display Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        choice = input("Select an option: ")

        if choice == '1':
            account.display_balance()
        elif choice == '2':
            amount = float(input("Enter deposit amount: "))
            account.deposit(amount)
        elif choice == '3':
            amount = float(input("Enter withdrawal amount: "))
            account.withdraw(amount)
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()
