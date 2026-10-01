from config import LOW_STOCK_LEVEL, HIGH_STOCK_LEVEL
from repositories.csv_repository import CSVRepository
from utilities.inventory_utilities import (
    get_low_stock_products,
    get_high_stock_products
)


class StockService:

    def __init__(self, repository: CSVRepository):
        self.repository = repository

    def check_low_stock(self) -> None:
        products = self.repository.read_products()

        if not products:
            print("No products available.")
            return

        products = get_low_stock_products(products)

        if not products:
            print("No low-stock products.")
            return

        print("LOW STOCK")
        print(f"Low-stock threshold: {LOW_STOCK_LEVEL}")

        for product in products:
            print(
                f"{product['product_id']} | "
                f"{product['product_name']} | "
                f"Stock: {product['quantity']}"
            )

    def check_high_stock(self) -> None:
        products = self.repository.read_products()

        if not products:
            print("No products available.")
            return

        products = get_high_stock_products(products)

        if not products:
            print("No high-stock products.")
            return

        print("HIGH STOCK")
        print(f"High-stock threshold: {HIGH_STOCK_LEVEL}")

        for product in products:
            print(
                f"{product['product_id']} | "
                f"{product['product_name']} | "
                f"Stock: {product['quantity']}"
            )

    def check_out_of_stock(self):
        products = self.repository.read_products()
        if not products:
            print("No products available. ")
            return

        has_out_of_stock = any(product["quantity"]==0 for product in products)

        if has_out_of_stock:
            print("Some products are out of stock.")

            out_of_stock_products = [
                product for product in products
                if product["quantity"] == 0
            ]

            for product in out_of_stock_products:
                print(
                    f"{product['product_id']} | "
                    f"{product['product_name']}"
                )

        else:
            print("No products are out of stock.")

        