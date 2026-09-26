from utils.inventory import APP_NAME

from utils.view import (
    view_products,
    view_stock
)

from utils.add import (
    add_stock
)

from utils.update import (
    update_stock
)

from utils.delete import (
    delete_stock
)

from utils.low_stock import (
    check_low_stock
)


from utils.search import (
    search_product
)



def display_menu():

    print(f" {APP_NAME} ")
    print("1. View Products")
    print("2. View Stock")
    print("3. Add Stock Record")
    print("4. Update Stock")
    print("5. Delete Stock Record")
    print("6. Low stock record")
    print("7. Search product")
    print("8. Exit")


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
                # pass
                update_stock()

            case 5:
                # pass
                delete_stock()

            case 6:
                check_low_stock()
                

            case 7:
                search_product()

            case 8:
                print("Thank you!")
                break

            case _:
                print("Invalid choice. Choose from 1 to 6 only")

        
    except Exception as error:

        print( f"Unexpected error occurred: {error}")
