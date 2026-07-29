class BankAccount:
    def __init__(self):
        
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds.")

    def check_balance(self):
        print(f"Current balance: ${self.balance:.2f}")

def main():
    account = BankAccount()
    while True:
        print("\n--- Bank Account Management System ---")
        print("1. Deposit")
        print("2. withdraw")
        print("3.Check Balance")
        print("4. Exit")
        
        input_choice = input("Enter your choice (1-4): ")
        
        if input_choice == '1':
            amount = float(input("Enter the amount to deposit: $"))
            account.deposit(amount)
            print("depositing funds...")
        elif input_choice == '2':
            amount = float(input("enter the amount to withdraw: $ "))
            account.withdraw(amount)
            print("withdrawing funds...")
        elif input_choice == '3':
            account.check_balance()
            print("checking funds...")
        elif input_choice == '4':
            print("Exiting the banking system. Thank you for using our services!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")
            
if __name__ == "__main__":
    main()      