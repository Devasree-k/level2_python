from config import APP_NAME

from utils.common import Common
from utils.product import Product
from utils.order import Order
from utils.search import Search
from utils.low_stock import LowStock
from utils.report import Report


# from utils.product import view_products
# from utils.order import (
#     place_order,
#     view_orders
# )
# from utils.search import search_product
# from utils.low_stock import (
#     check_low_stock
#     # generate_low_stock_report
# )
# # from utils.report import (
# #     # generate_order_report,
# #     calculate_inventory_value
# # )

class App:
    def __init__(self):
        self.common = Common()
        self.product = Product(self.common)
        self.order = Order(self.common, self.product)
        self.search = Search(self.common, self.product)
        self.low_stock = LowStock(self.common)
        self.report = Report(self.common)

    def display_menu(self) -> None:

        print(f"  {APP_NAME}   ")
        print("1. View Products")
        print("2. Place Order")
        print("3. View Orders")
        print("4. Search Product")
        print("5. Check Low Stock")
        print("6. Generate inventory and low stock report")
        print("0. Exit")

    def run(self)->None:
        while True:
            self.display_menu()

            try:
                choice = int(input("Enter your choice: "))

                match choice:
                    case 1:
                        # view_products()
                        self.product.view_products()

                    case 2:
                        # place_order()
                        self.order.place_order()

                    case 3:
                        # view_orders()
                        self.order.view_orders()

                    case 4:
                        # search_product()
                        self.search.search_product()

                    case 5:
                        # check_low_stock()
                        self.low_stock.check_low_stock()

                    case 6:
                        self.report.generate_report()

                    case 0:
                        print("Thank you")
                        break

                    case _:
                        print("Invalid choice. Please choose 0-8.")

            except ValueError:
                print("Invalid input. Please enter a number.")

            except KeyboardInterrupt:
                print("Program interrupted.")
                break

            except Exception as error:
                print("Unexpected error occurred: "f"{error}")


if __name__ == "__main__":
    app = App()
    app.run()


