class User:
    def __init__(self, user_id, pin, balance=0.0):
        self.user_id = user_id
        self.pin = pin
        self.balance = balance
        self.transaction_history = []

class ATM:
    def __init__(self, users):
        self.users = users  # List of User objects

    def authenticate_user(self, user_id, pin):
        for user in self.users:
            if user.user_id == user_id and user.pin == pin:
                return user
        return None

    def display_menu(self):
        print("\nATM Menu:")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Transfer")
        print("5. Transactions History")
        print("6. Quit")

    def check_balance(self, user):
        print(f"Your balance: ${user.balance:.2f}")

    def deposit(self, user, amount):
        user.balance += amount
        user.transaction_history.append(f"Deposited ${amount:.2f}")

    def withdraw(self, user, amount):
        if user.balance >= amount:
            user.balance -= amount
            user.transaction_history.append(f"Withdrew ${amount:.2f}")
        else:
            print("Insufficient balance.")

    def transfer(self, user, recipient_user_id, amount):
        recipient = None
        for u in self.users:
            if u.user_id == recipient_user_id:
                recipient = u
                break
        if recipient:
            if user.balance >= amount:
                user.balance -= amount
                recipient.balance += amount
                user.transaction_history.append(f"Transferred ${amount:.2f} to {recipient_user_id}")
                recipient.transaction_history.append(f"Received ${amount:.2f} from {user.user_id}")
            else:
                print("Insufficient balance.")
        else:
            print("Recipient user ID not found.")

    def display_transaction_history(self, user):
        print("Transaction History:")
        for transaction in user.transaction_history:
            print(transaction)

    def start(self):
        print("Welcome to the ATM!")
        while True:
            user_id = input("Enter your user ID: ")
            pin = input("Enter your PIN: ")

            user = self.authenticate_user(user_id, pin)
            if user:
                print(f"Welcome, {user_id}!")
                break
            else:
                print("Invalid user ID or PIN. Please try again.")

        while True:
            self.display_menu()
            choice = input("Enter your choice (1-6): ")

            if choice == '1':
                self.check_balance(user)
            elif choice == '2':
                amount = float(input("Enter deposit amount: $"))
                self.deposit(user, amount)
            elif choice == '3':
                amount = float(input("Enter withdrawal amount: $"))
                self.withdraw(user, amount)
            elif choice == '4':
                recipient_user_id = input("Enter recipient's user ID: ")
                amount = float(input("Enter transfer amount: $"))
                self.transfer(user, recipient_user_id, amount)
            elif choice == '5':
                self.display_transaction_history(user)
            elif choice == '6':
                print("Thank you for using the ATM!")
                break
            else:
                print("Invalid choice. Please try again.")

# Example usage:
users = [
    User("123456", "1234", 1000.0),
    User("987654", "5678", 500.0)
]

atm = ATM(users)
atm.start()
