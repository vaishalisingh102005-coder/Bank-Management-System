class BankAccount:
    def __init__(self, name, account_no, balance=0):
        self.name = name
        self.account_no = account_no
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Amount deposited successfully.")
        else:
            print("Invalid amount.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid amount.")
        elif amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print("Amount withdrawn successfully.")

    def check_balance(self):
        print("Current Balance:", self.balance)

    def display_details(self):
        print("\nAccount Holder:", self.name)
        print("Account Number:", self.account_no)
        print("Balance:", self.balance)


name = input("Enter account holder name: ")
account_no = input("Enter account number: ")
balance = float(input("Enter initial balance: "))

account = BankAccount(name, account_no, balance)

while True:
    print("\nBank Management System")
    print("1. Deposit Money")
    print("2. Withdraw Money")
    print("3. Check Balance")
    print("4. Display Account Details")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        amount = float(input("Enter amount to deposit: "))
        account.deposit(amount)

    elif choice == 2:
        amount = float(input("Enter amount to withdraw: "))
        account.withdraw(amount)

    elif choice == 3:
        account.check_balance()

    elif choice == 4:
        account.display_details()

    elif choice == 5:
        print("Thank you for using Bank Management System.")
        break

    else:
        print("Invalid choice.")
