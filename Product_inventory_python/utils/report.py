

from config import REPORT_FILE, LOW_STOCK_LEVEL
from utils.common import Common

class Report:
    def __init__(self, common: Common):
        self.common = common

    def get_low_stock_products(self, products: list[dict]) -> list[dict]:
        return [
            product
            for product in products
            if product["quantity"] <= LOW_STOCK_LEVEL
        ]

    def calculate_inventory_value(self, products: list[dict]) -> float:
        return sum(
            product["price"] * product["quantity"]
            for product in products
        )

    def generate_report(self) -> None:
        products = self.common.read_products()
        if not products:
            print("No products available.")
            return

        total_products = len(products)
        total_units = sum(product["quantity"] for product in products)
        total_inventory_value = self.calculate_inventory_value(products)

        products_by_value = sorted(
            products,
            key=lambda product: product["price"] * product["quantity"],
            reverse=True
        )

        low_stock_products = self.get_low_stock_products(products)
        low_stock_products.sort(key=lambda product: product["quantity"])

        try:
            with open(REPORT_FILE, "w",encoding="utf-8") as file:
                file.write("=" * 50 + "\n")
                file.write("              INVENTORY REPORT\n")
                file.write("=" * 50 + "\n\n")
                file.write(f"Total Products  : {total_products}\n")
                file.write(f"Total Units     : {total_units}\n")
                file.write(f"Inventory Value : {total_inventory_value:.2f}")
                file.write("PRODUCT DETAILS\n")
                file.write("-" * 50 + "\n\n")

                for product in products_by_value:
                    product_value = product["price"] * product["quantity"]
                    file.write(f"Product ID : {product['product_id']}\n")
                    file.write(f"Product    : {product['product_name']}\n")
                    file.write(f"Category   : {product['category']}\n")
                    file.write(f"Price      : ₹{product['price']:.2f}\n")
                    file.write(f"Quantity   : {product['quantity']}\n")
                    file.write(f"Stock Value: ₹{product_value:.2f}\n")
                    file.write("-" * 50 + "\n")

                file.write("\n" + "=" * 50 + "\n")
                file.write("              LOW STOCK REPORT\n")
                file.write("=" * 50 + "\n\n")
                file.write(f"Low Stock Level : {LOW_STOCK_LEVEL}\n\n")

                if not low_stock_products:
                    file.write("No low-stock products.\n")
                else:
                    file.write(f"Total Low Stock Products : {len(low_stock_products)}\n\n")
                    for product in low_stock_products:
                        file.write(f"Product ID : {product['product_id']}\n")
                        file.write(f"Product    : {product['product_name']}\n")
                        file.write(f"Category   : {product['category']}\n")
                        file.write(f"Quantity   : {product['quantity']}\n")
                        file.write("-" * 50 + "\n")

                file.write("\n" + "=" * 50 + "\n")
                file.write("              END OF REPORT\n")
                file.write("=" * 50 + "\n")

            print("Complete report generated successfully.")
            print(f"Report location: {REPORT_FILE}")

        except OSError as error:
            print(f"Unable to generate report: {error}")