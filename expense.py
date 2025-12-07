expenses = []   # list to store all expenses

while True:
    print("\n========== Expense Tracker ==========")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View Total Amount Spent")
    print("4. View Expenses by Category")
    print("5. Exit")
    print("=====================================")

    choice = input("Enter your choice (1-5): ")

    # 1. Add Expense
    if choice == "1":
        amount = int(input("Enter amount: "))
        category = input("Enter category: ")
        description = input("Enter description: ")

        expense = {
            "amount": amount,
            "category": category,
            "description": description
        }

        expenses.append(expense)
        print("\n✔ Expense Added Successfully!")

    # 2. View All Expenses
    elif choice == "2":
        if not expenses:
            print("\n❗ No expenses recorded.")
        else:
            print("\n----- All Expenses -----")
            for i, exp in enumerate(expenses, start=1):
                print(f"{i}. Amount: {exp['amount']} | Category: {exp['category']} | Description: {exp['description']}")

    # 3. Total Amount Spent
    elif choice == "3":
        if not expenses:
            print("\n❗ No expenses to calculate.")
        else:
            total = sum(exp["amount"] for exp in expenses)
            print(f"\n💰 Total Amount Spent: {total}")

    # 4. View Expenses by Category
    elif choice == "4":
        if not expenses:
            print("\n❗ No expenses recorded yet.")
        else:
            category_name = input("Enter category name: ")
            found = False
            category_total = 0

            print(f"\n----- Expenses under '{category_name}' -----")
            for exp in expenses:
                if exp["category"].lower() == category_name.lower():
                    print(f"Amount: {exp['amount']} | Description: {exp['description']}")
                    category_total += exp["amount"]
                    found = True

            if found:
                print(f"📌 Total spent in this category: {category_total}")
            else:
                print("❗ No expenses found for this category.")

    # 5. Exit
    elif choice == "5":
        print("\n👋 Exiting program... Goodbye!")
        break

    else:
        print("\n❗ Invalid choice. Please enter a number between 1-5.")

