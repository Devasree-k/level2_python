# Mini Banking Application

account = {}

while True:

    print("MINI BANKING APPLICATION")
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check Balance")
    print("5. Transaction History")
    print("6. Exit")

    choice = input("Enter your choice: ")

    match choice:

        case "1":
            # Create Account

            if account:
                print("Account already exists!")

            else:
                account_number = input("Enter account number: ")
                name = input("Enter account holder name: ")

                while True:
                    balance = float(input("Enter initial deposit: "))

                    if balance >= 0:
                        break
                    else:
                        print("Initial deposit cannot be negative.")

                account = {
                    "account_number": account_number,
                    "name": name,
                    "balance": balance,
                    "transactions": []
                }

                if balance > 0:
                    account["transactions"].append( f"Initial deposit: ₹{balance}")

                print("Account created successfully!")

        case "2":
            # Deposit

            if not account:
                print("Please create an account first.")

            else:
                while True:
                    amount = float(input("Enter deposit amount: "))

                    if amount > 0:
                        account["balance"] += amount
                        account["transactions"].append( f"Deposited: ₹{amount}" )
                        print("Deposit successful!")
                        break
                    else:
                        print("Amount must be greater than 0.")

        case "3":
            # Withdraw

            if not account:
                print("Please create an account first.")

            else:
                while True:
                    amount = float(input("Enter withdrawal amount: "))

                    if amount <= 0:
                        print("Amount must be greater than 0.")

                    elif amount > account["balance"]:
                        print("Insufficient balance!")

                    else:
                        account["balance"] -= amount
                        account["transactions"].append( f"Withdrawn: ₹{amount}")
                        print("Withdrawal successful!")
                        break

        case "4":
            # Check Balance

            if not account:
                print("Please create an account first.")

            else:
                print("ACCOUNT DETAILS")
                print("Account Number:", account["account_number"])
                print("Account Holder:", account["name"])
                print("Balance: ₹", account["balance"])

        case "5":
            # Transaction History

            if not account:
                print("Please create an account first.")

            else:
                print("TRANSACTION HISTORY")

                if not account["transactions"]:
                    print("No transactions found.")

                else:
                    for transaction in account["transactions"]:
                        print(transaction)

        case "6":
            print("Thank you for using the banking application!")
            break

        case _:
            print("Invalid choice! Please enter 1 to 6.")