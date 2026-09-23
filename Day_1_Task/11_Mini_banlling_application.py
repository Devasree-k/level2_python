# Mini Banking Application

accounts = []


def create_account():
    account_number = input("Enter account number: ")

    # Check whether account already exists
    for account in accounts:
        if account["account_number"] == account_number:
            print("Account already exists!")
            return

    name = input("Enter account holder name: ")

    # Validate initial deposit
    while True:
        try:
            balance = float(input("Enter initial deposit: "))

            if balance >= 0:
                break
            else:
                print("Initial deposit cannot be negative.")

        except ValueError:
            print("Please enter a valid amount.")

    account = {
        "account_number": account_number,
        "name": name,
        "balance": balance,
        "transactions": []
    }

    # Add initial transaction
    if balance > 0:
        account["transactions"].append(
            f"Initial deposit: ₹{balance:.2f}"
        )

    accounts.append(account)

    print("Account created successfully!")


def find_account():
    account_number = input("Enter account number: ")

    for account in accounts:
        if account["account_number"] == account_number:
            return account

    return None


def deposit():
    account = find_account()

    if account is None:
        print("Account not found!")
        return

    while True:
        try:
            amount = float(input("Enter deposit amount: "))

            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")

        except ValueError:
            print("Please enter a valid amount.")

    account["balance"] += amount

    account["transactions"].append(
        f"Deposited: ₹{amount:.2f}"
    )

    print("Deposit successful!")
    print("New Balance: ₹", account["balance"])


def withdraw():
    account = find_account()

    if account is None:
        print("Account not found!")
        return

    while True:
        try:
            amount = float(input("Enter withdrawal amount: "))

            if amount <= 0:
                print("Amount must be greater than 0.")

            elif amount > account["balance"]:
                print("Insufficient balance!")

            else:
                break

        except ValueError:
            print("Please enter a valid amount.")

    account["balance"] -= amount

    account["transactions"].append(
        f"Withdrawn: ₹{amount:.2f}"
    )

    print("Withdrawal successful!")
    print("Remaining Balance: ₹", account["balance"])


def check_balance():
    account = find_account()

    if account is None:
        print("Account not found!")
        return

    print("\n===== ACCOUNT DETAILS =====")
    print("Account Number:", account["account_number"])
    print("Account Holder:", account["name"])
    print("Balance: ₹", account["balance"])


def transaction_history():
    account = find_account()

    if account is None:
        print("Account not found!")
        return

    print("\n===== TRANSACTION HISTORY =====")

    if not account["transactions"]:
        print("No transactions found.")
    else:
        for transaction in account["transactions"]:
            print(transaction)


# Main Menu
while True:

    print("\n===== MINI BANKING APPLICATION =====")
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check Balance")
    print("5. Transaction History")
    print("6. Exit")

    choice = input("Enter your choice: ")

    match choice:

        case "1":
            create_account()

        case "2":
            deposit()

        case "3":
            withdraw()

        case "4":
            check_balance()

        case "5":
            transaction_history()

        case "6":
            print("Thank you for using the banking application!")
            break

        case _:
            print("Invalid choice! Please enter 1 to 6.")



