
customer_name = input("Enter the customer name : ")
units_consumed = float(input("Enter the no.of units consumed : "))

if units_consumed < 0:
    print("Units consumed cannot be negative. ")
else:
    if units_consumed <= 100:
        charge = 0
    elif units_consumed <= 400:
        charge = (units_consumed - 100) * 4.5
    elif units_consumed <= 700:
        charge = ( 300 * 4.5 ) + ( units_consumed - 400 ) * 6
    else:
        charge = ( 300 * 4.5 ) + ( 300 * 6 ) + (units_consumed - 700 ) * 9

    tax = charge * 0.05
    total_charges = charge + tax

    print("\nElectricity Bill")
    print("Customer Name :", customer_name)
    print("Units Consumed:", units_consumed)
    print("Energy Charge :", charge)
    print("Tax           :", tax)
    print("Total Bill    :", total_charges)
