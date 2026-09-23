# Menu-Based Number Analyzer

def check_even_odd(num):
    if num % 2 == 0:
        print("Even Number")
    else:
        print("Odd Number")


def check_prime(num):
    if num < 2:
        print("Not Prime")
        return

    for i in range(2, num):
        if num % i == 0:
            print("Not Prime")
            return

    print("Prime")


def check_palindrome(num):
    original = num
    reverse = 0

    while num > 0:
        digit = num % 10
        reverse = reverse * 10 + digit
        num //= 10

    if original == reverse:
        print("Palindrome")
    else:
        print("Not Palindrome")


def check_armstrong(num):
    original = num
    digits = len(str(num))
    total = 0

    while num > 0:
        digit = num % 10
        total += digit ** digits
        num //= 10

    if total == original:
        print("Armstrong")
    else:
        print("Not Armstrong")


def reverse_number(num):
    reverse = 0

    while num > 0:
        digit = num % 10
        reverse = reverse * 10 + digit
        num //= 10

    print("Reverse:", reverse)


def sum_of_digits(num):
    total = 0

    while num > 0:
        digit = num % 10
        total += digit
        num //= 10

    print("Sum of digits:", total)


while True:

    print("\n===== NUMBER ANALYZER =====")
    print("1. Check Even/Odd")
    print("2. Check Prime")
    print("3. Check Palindrome")
    print("4. Check Armstrong")
    print("5. Reverse Number")
    print("6. Sum of Digits")
    print("7. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 7:
        print("Thank you!")
        break

    num = int(input("Enter a number: "))

    match choice:
        case 1:
            check_even_odd(num)

        case 2:
            check_prime(num)

        case 3:
            check_palindrome(num)

        case 4:
            check_armstrong(num)

        case 5:
            reverse_number(num)

        case 6:
            sum_of_digits(num)

        case _:
            print("Invalid choice! Please select 1 to 7.")


