from config import APP_NAME

import asyncio

from exceptions.inventory_exceptions import (ProductNotFoundError, InsufficientStockError, InventoryError)

from repositories.json_repository import JSONRepository

from services.product_services import ProductService
from services.orders_services import OrderService
from services.search_services import SearchService
from services.stock_service import StockService
from services.report_service import ReportService
from services.product_detail_service import ProductDetailService

from utilities.logging_config import setup_logging
import logging
logger = logging.getLogger(__name__)


class App:

    def __init__(self):
        self.repository = JSONRepository()

        self.product = ProductService(self.repository)
        self.order = OrderService(self.repository, self.product)
        self.search = SearchService(self.repository, self.product)
        self.stock = StockService(self.repository)
        self.report = ReportService(self.repository)
        self.product_detail = ProductDetailService(self.repository)

    def display_menu(self) -> None:
        print(f"  {APP_NAME}   ")
        print("1. View Products")
        print("2. Place Order")
        print("3. View Orders")
        print("4. Search Product by ID")
        print("5. Search Product by Name")
        print("6. Check Low Stock")
        print("7. Check High Stock")
        print("8. Generate inventory and low stock report")
        print("9. Display product details")
        print("0. Exit")

    async def run(self) -> None:
        while True:
            self.display_menu()

            try:
                choice = int(input("Enter your choice: "))

                match choice:
                    case 1:
                        await self.product.view_products()

                    case 2:
                        await self.order.place_order()

                    case 3:
                        self.order.view_orders()

                    case 4:
                        await self.search.search_product()

                    case 5:
                        await self.search.search_by_name()

                    case 6:
                        await self.stock.check_low_stock()

                    case 7:
                        await self.stock.check_high_stock()

                    case 8:
                        await self.report.generate_report()

                    case 9:
                        await self.product_detail.display_product_details()

                    case 0:
                        logger.info("Product Inventory application stopped")
                        print("Thank you")
                        break

                    case _:
                        print("Invalid choice. Please choose 0-9.")

            except ValueError:
                print("Invalid input. Please enter a number.")

            except KeyboardInterrupt:
                print("Program interrupted.")
                break

            except InventoryError as e:
                print(f"Inventory Issue : {e}")

            # except Exception as error:
            #     print(f"Unexpected error occurred: {error}")


if __name__ == "__main__":
    setup_logging()
    app = App()
    # app.run()
    asyncio.run(app.run())

