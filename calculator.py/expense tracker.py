class Expense: 
     def __init__(self, date, amount, description):
         self.date = date
         self.amount = amount
         self.description = description 

class ExpenseTracker:
     def __init__(self):
         self.expenses = []

     def add_expense(self, expense):
         self.expenses.append(expense)

     def remove_expense(self, index):
         if 0 <= index < len(self.expenses): 
             del self.expenses[index]
             print("Expense removed successfully.")
         else:
            print("Invalid expense index.")

     def view_expenses(self):
        if len(self.expenses) == 0:
           print("No expenses found.")
        else:
            print("Expense List:")
            for i, expense in enumerate(self.expenses, start=1):
                print(f"{i}. Date: {expense.date}, Amount: {expense.amount}, Description: {expense.description}")

     def total_expenses(self):
         total = sum(expense.amount for expense in self.expenses)
         print("Total Expenses: ${:.2f}".format(total))
    def main():
        tracker = ExpenseTracker()

        while True:
            print("\nExpense Tracker Menu:")
            print("1. Add Expense")
            print("2. Remove Expense")
            print("3. View Expenses")
            print("4. Total Expenses")
            print("5. Exit")

            choice = input("Enter your choice (1-5): ")

            if choice == '1': 
                date = input("Enter the date (YYYY-MM-DD): ")
                description = input("Enter the description: ")
                amount = float(input("Enter the amount: "))
                expense = Expense(date, amount, description)
                tracker.add_expense(expense)
                print("Expense added successfully.")
            elif choice == '2':
                index = int(input("Enter the index of the expense to remove: ")) -1 
                tracker.remove_expense(index)
            elif choice == '3': 
                tracker.view_expenses()
            elif choice == '4':
                tracker.total_expenses()
            elif choice == '5':
                print("Exiting the Expense Tracker. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
                