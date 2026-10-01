
attempt = 0
max_attempt = 3

while attempt < max_attempt:
    pin = input("Enter the password ")
    if pin == "qwert1234":
        print("Login Successful")
        break
    else:
        attempt += 1
        print("Invalid Passsord ")

if attempt == max_attempt:
    print("Account is locked")

else:

    balance = 3000

    while True:
        print("The choices are :")
        print("1. Check Balance ")
        print("2. Deposit ")
        print("3. Withdraw ")
        print("4. Change PIN ")
        print("5. Exit ")

        choice = int(input("Enter your choice : "))
        match choice:
            case 1:
                print(f"Your current balance is {balance}")
            case 2:
                deposit_amount = float(input("Enter the amount to deposit :"))
                if deposit_amount > 0:
                    balance += deposit_amount
                    print(f"Amount deposited successfully. \nThe avaiable balance is {balance}")
                else:
                    print("Amount should not be negative number. ")
            case 3:
                withdraw_amount = float(input("Enter the withdraw amount :"))
                if withdraw_amount > 0 and withdraw_amount <= balance:
                    balance -= withdraw_amount
                    print(f"Amount withdrawn successfully. \nThe availale balance is {balance}")
                else:
                    print("The withdraw amount exceeds the total amount")
            case 4:
                current_pin = input("Enter your current PIN : ")
                if current_pin == pin:
                    new_pin = input("Enter your new PIN : ")
                    pin = new_pin
                    print("PIN changed successfully ")
                else:
                    print("Incorrect current pin ")
            case 5:
                print("Thank you ....")
                break

            case _:
                print("Invalid choice ")
                