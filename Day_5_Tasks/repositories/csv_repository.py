import csv

from config import PRODUCT_FILE, ORDER_FILE

class CSVRepository:

    def read_products(self) -> list[dict]:
        products = []

        try:
            with open(PRODUCT_FILE, "r") as file:
                reader = csv.DictReader(file)

                for row in reader:
                    row["price"] = float(row["price"])
                    row["quantity"] = int(row["quantity"])
                    products.append(row)

        except FileNotFoundError:
            print("Product file not found.")

        except ValueError:
            print("Invalid numeric data found in product.csv.")

        return products

    def write_products(self, products: list[dict]) -> None:
        fieldnames = [
            "product_id", "product_name", "category",
            "price", "quantity"
        ]

        try:
            with open(PRODUCT_FILE, "w") as file:
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(products)

        except OSError as error:
            print(f"Unable to save products: {error}")

    def read_orders(self) -> list[dict]:
        orders = []
        try:
            with open(ORDER_FILE, "r") as file:
                reader = csv.DictReader(file)

                for row in reader:
                    row["quantity"] = int(row["quantity"])
                    row["unit_price"] = float(row["unit_price"])
                    row["total_amount"] = float(row["total_amount"])
                    orders.append(row)

        except FileNotFoundError:
            print("Orders file not found.")
        except ValueError:
            print("Invalid numeric data found in orders.csv.")
        return orders


    def write_orders(self, orders: list[dict]) -> None:
        fieldnames = ["order_id", "product_id", "quantity",
                    "unit_price", "total_amount", "status"
        ]
        try:
            with open(ORDER_FILE, "w") as file:
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(orders)
                
        except OSError as error:
            print(f"Unable to save orders: {error}")