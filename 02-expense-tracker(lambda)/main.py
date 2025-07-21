# main.py

def add_expense(expenses, amount, category):
    expenses.append({'amount': amount, 'category': category})
    
def print_expenses(expenses):
    for expense in expenses:
        print(f'Amount: ₹{expense["amount"]}, Category: {expense["category"]}')
    
def total_expenses(expenses):
    return sum(map(lambda expense: expense['amount'], expenses))
    
def filter_expenses_by_category(expenses, category):
    return filter(lambda expense: expense['category'].lower() == category.lower(), expenses)
    
def main():
    expenses = []

    while True:
        print('\nExpense Tracker Menu')
        print('1. Add an expense')
        print('2. List all expenses')
        print('3. Show total expenses')
        print('4. Filter expenses by category')
        print('5. Exit')
       
        choice = input('Enter your choice (1-5): ')

        if choice == '1':
            try:
                amount = float(input('Enter amount: ₹'))
                category = input('Enter category: ')
                add_expense(expenses, amount, category)
                print('Expense added successfully.')
            except ValueError:
                print('Invalid amount. Please enter a number.')

        elif choice == '2':
            if expenses:
                print('\nAll Expenses:')
                print_expenses(expenses)
            else:
                print('No expenses recorded yet.')

        elif choice == '3':
            print(f'\nTotal Expenses: ₹{total_expenses(expenses)}')

        elif choice == '4':
            category = input('Enter category to filter: ')
            expenses_from_category = filter_expenses_by_category(expenses, category)
            filtered = list(expenses_from_category)
            if filtered:
                print(f'\nExpenses for category "{category}":')
                print_expenses(filtered)
            else:
                print(f'No expenses found for category "{category}".')

        elif choice == '5':
            print('Exiting... Thank you for using Expense Tracker.')
            break

        else:
            print('Invalid choice. Please enter a number from 1 to 5.')

if __name__ == '__main__':
    main()
