from utils.view import (
    # APP_NAME,
    view_products,
    view_stock,
    add_stock,
    # update_stock,
    # delete_stock
)


def display_menu():

    # print(f" {APP_NAME} ")
    print("1. View Products")
    print("2. View Stock")
    print("3. Add Stock Record")
    print("4. Update Stock")
    print("5. Delete Stock Record")
    print("0. Exit")


while True:

    display_menu()

    choice = int(input( "Enter your choice: "))

    try:

        match choice:
            case 1:
                view_products()

            case 2:
                view_stock()

            case 3:
                # pass
                add_stock()

            case 4:
                pass
                # update_stock()

            case 5:
                pass
                # delete_stock()

            case 6:
                print("Thank you!")
                break

            case _:
                print("Invalid choice. Choose from 1 to 6 only")

        
    except Exception as error:

        print( f"Unexpected error occurred: {error}")
