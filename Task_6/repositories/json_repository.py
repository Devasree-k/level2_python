import asyncio
import json

from pydantic import ValidationError

from config import PRODUCT_FILE, ORDER_FILE
from models.product_model import Product
from models.order_model import Order


class JSONRepository:

    async def read_products(self) -> list[Product]:
        products = []

        try:
            await asyncio.sleep(0)

            with open(PRODUCT_FILE, "r", encoding="utf-8") as file:
                data = json.load(file)

            products = [
                Product(**product)
                for product in data
            ]

        except FileNotFoundError:
            print("Product file not found.")

        except json.JSONDecodeError:
            print("Invalid JSON data found in product.json.")

        except ValidationError as error:
            print("Invalid product data.")
            print(error)

        return products

    def write_products(self, products: list[Product]) -> None:
        try:
            with open(PRODUCT_FILE, "w", encoding="utf-8") as file:
                json.dump([product.model_dump() for product in products], file, indent=4)

        except OSError as error:
            print(f"Unable to save products: {error}")

    def read_orders(self) -> list[Order]:
        orders = []

        try:
            with open(ORDER_FILE, "r", encoding="utf-8") as file:
                data = json.load(file)

            orders = [
                Order(**order)
                for order in data
            ]

        except FileNotFoundError:
            print("Orders file not found.")

        except json.JSONDecodeError:
            print("Invalid JSON data found in orders.json.")

        except ValidationError as error:
            print("Invalid order data.")
            print(error)

        return orders

    def write_orders(self, orders: list[Order]) -> None:
        try:
            with open(ORDER_FILE, "w", encoding="utf-8") as file:
                json.dump( [order.model_dump() for order in orders], file, indent=4 )

        except OSError as error:
            print(f"Unable to save orders: {error}")

            