account: dict = {}

def create_account(account: dict) -> dict:

    if account:
        print("Account already exists!")
        return account

    account_number: str = input("Enter account number: ")
    name: str = input("Enter account holder name: ")

    while True:
        balance: float = float(input("Enter initial deposit: "))
        if balance >= 0:
            break
        print("Initial deposit cannot be negative.")

    account = {
        "account_number": account_number,
        "name": name,
        "balance": balance,
        "transactions": []
    }

    if balance > 0:
        account["transactions"].append(
            f"Initial deposit: ₹{balance}"
        )
    print("Account created successfully!")

    return account


def deposit(account: dict) -> None:

    if not account:
        print("Please create an account first.")
        return

    while True:

        amount: float = float(input("Enter deposit amount: "))

        if amount > 0:
            account["balance"] += amount
            account["transactions"].append(
                f"Deposited: ₹{amount}"
            )

            print("Deposit successful!")
            print("New Balance: ₹", account["balance"])
            break

        print("Amount must be greater than 0.")


def withdraw(account: dict) -> None:

    if not account:
        print("Please create an account first.")
        return

    while True:

        amount: float = float(input("Enter withdrawal amount: "))
        if amount <= 0:
            print("Amount must be greater than 0.")

        elif amount > account["balance"]:
            print("Insufficient balance!")

        else:
            account["balance"] -= amount
            account["transactions"].append(
                f"Withdrawn: ₹{amount}"
            )

            print("Withdrawal successful!")
            print("Remaining Balance: ₹", account["balance"])
            break


def check_balance(account: dict) -> None:

    if not account:
        print("Please create an account first.")
        return

    print("\nACCOUNT DETAILS")
    print("Account Number:", account["account_number"])
    print("Account Holder:", account["name"])
    print("Balance: ₹", account["balance"])


def transaction_history(account: dict) -> None:

    if not account:
        print("Please create an account first.")
        return

    print("\nTRANSACTION HISTORY")

    if not account["transactions"]:
        print("No transactions found.")
        return

    for transaction in account["transactions"]:
        print(transaction)


while True:

    print("MINI BANKING APPLICATION")
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check Balance")
    print("5. Transaction History")
    print("6. Exit")

    choice: str = input("Enter your choice: ")

    match choice:

        case "1":
            account = create_account(account)

        case "2":
            deposit(account)

        case "3":
            withdraw(account)

        case "4":
            check_balance(account)

        case "5":
            transaction_history(account)

        case "6":
            print("Thank you for using the banking application!")
            break

        case _:
            print("Invalid choice! Please enter 1 to 6.")