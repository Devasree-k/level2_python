from config import REPORT_FILE, LOW_STOCK_LEVEL
from repositories.json_repository import JSONRepository
from utilities.inventory_utilities import get_low_stock_products

from models.product_model import Product

class ReportService:

    def __init__(self, repository: JSONRepository):
        self.repository = repository

    def calculate_inventory_value(self, products: list[Product]) -> float:
        return sum(
            product["price"] * product["quantity"]
            for product in products
        )

    async def generate_report(self) -> None:
        products = await self.repository.read_products()

        if not products:
            print("No products available.")
            return

        total_products = len(products)
        total_units = sum(product["quantity"] for product in products)
        total_value = self.calculate_inventory_value(products)

        products_by_value = sorted(
            products,
            key=lambda product: product["price"] * product["quantity"],
            reverse=True
        )

        low_stock_products = get_low_stock_products(products)
        low_stock_products.sort(key=lambda product: product["quantity"])

        try:
            REPORT_FILE.parent.mkdir(parents=True, exist_ok=True)

            with open(REPORT_FILE, "w", encoding="utf-8") as file:

                file.write("\n INVENTORY REPORT\n\n")

                file.write(f"Total Products  : {total_products}\n")
                file.write(f"Total Units     : {total_units}\n")
                file.write(f"Inventory Value : ₹{total_value:.2f}\n")

                file.write("\nPRODUCT DETAILS\n\n")

                for product in products_by_value:
                    product_value = product["price"] * product["quantity"]

                    file.write(f"Product ID : {product.product_id}\n")
                    file.write(f"Product    : {product.product_name}\n")
                    file.write(f"Category   : {product.category}\n")
                    file.write(f"Price      : ₹{product.price:.2f}\n")
                    file.write(f"Quantity   : {product.quantity}\n")
                    file.write(f"Stock Value: ₹{product_value:.2f}\n\n")

                file.write("\n LOW STOCK REPORT\n\n")

                file.write(f"Low Stock Level : {LOW_STOCK_LEVEL}\n\n")

                if not low_stock_products:
                    file.write("No low-stock products.\n")
                else:
                    file.write(
                        f"Total Low Stock Products : "
                        f"{len(low_stock_products)}\n\n"
                    )

                    for product in low_stock_products:
                        file.write(f"Product ID : {product.product_id}\n")
                        file.write(f"Product    : {product.product_name}\n")
                        file.write(f"Category   : {product.category}\n")
                        file.write(f"Quantity   : {product.quantity}\n")
                        file.write("-" * 50 + "\n")

            print("Complete report generated successfully.")
            print(f"Report location: {REPORT_FILE}")

        except OSError as error:
            print(f"Unable to generate report: {error}")