def analyze_number(n):
    # Handle negative numbers for specific properties
    is_negative = n < 0
    num = abs(n)
    
    # 1. Even/Odd
    is_even = "Even" if n % 2 == 0 else "Odd"
    
    # Extract digits for math operations
    digits = []
    if num == 0:
        digits = [0]
    else:
        temp = num
        while temp > 0:
            digits.insert(0, temp % 10)
            temp //= 10
            
    # 2. Number of digits
    num_digits = len(digits)
    
    # 3. Sum of digits
    sum_dig = sum(digits)
    
    # 4. Product of digits
    prod_dig = 1
    for d in digits:
        prod_dig *= d
        
    # 5. Reverse
    rev_num = 0
    temp = num
    while temp > 0:
        rev_num = (rev_num * 10) + (temp % 10)
    if is_negative:
        rev_num = -rev_num
        
    # 6. Palindrome
    is_palindrome = "Palindrome" if n == rev_num else "Not Palindrome"
    
    # 7. Armstrong Number (Sum of digits raised to the power of total digits)
    armstrong_sum = sum(d ** num_digits for d in digits)
    is_armstrong = "Armstrong" if (num == armstrong_sum and not is_negative) else "Not Armstrong"
    
    # 8. Prime Number
    is_prime = "Prime"
    if n <= 1:
        is_prime = "Not Prime"
    else:
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                is_prime = "Not Prime"
                break

    # Display Results
    print(f"Analysis for Number: {n}")
    print(f"--------------------------")
    print(f"Number of digits     : {num_digits}")
    print(f"Sum of digits        : {sum_dig}")
    print(f"Product of digits    : {prod_dig}")
    print(f"Reverse              : {rev_num}")
    print(f"Even/Odd             : {is_even}")
    print(f"Prime/Not Prime      : {is_prime}")
    print(f"Palindrome/Not       : {is_palindrome}")
    print(f"Armstrong/Not        : {is_strong}")

# Example Test Run
analyze_number(153)



