# from config import LOW_STOCK_LEVEL
# from utils.common import read_products

from config import LOW_STOCK_LEVEL
from utils.common import Common

class LowStock:
    def __init__(self, common: Common):
        self.common = common

    def get_low_stock_products(self, products: list[dict]) -> list[dict]:
        low_stock_products = []
        for product in products:
            if product["quantity"] <= LOW_STOCK_LEVEL:
                low_stock_products.append(product)
        return low_stock_products

    def check_low_stock(self) -> None:
        products = self.common.read_products()
        if not products:
            print("No products available.")
            return

        has_low_stock = any(
            product["quantity"] <= LOW_STOCK_LEVEL
            for product in products
        )

        if not has_low_stock:
            print("No low-stock products.")
            return

        low_stock_products = self.get_low_stock_products(products)
        low_stock_products.sort(key=lambda product: product["quantity"])

        print("LOW STOCK")
        print(f"Low-stock threshold: {LOW_STOCK_LEVEL}")
        print()

        for product in low_stock_products:
            print(f"{product['product_id']} | {product['product_name']} | Stock: {product['quantity']}")



# def get_low_stock_products(products: list[dict]) -> list[dict]:
#     low_stock_products = []

#     for product in products:
#         if product["quantity"] <= LOW_STOCK_LEVEL:
#             low_stock_products.append(product)

#     return low_stock_products


# def check_low_stock() -> None:
   
#     products = read_products()

#     if not products:
#         print("No products available.")
#         return

#     has_low_stock = any(
#         product["quantity"] <= LOW_STOCK_LEVEL
#         for product in products
#     )

#     if not has_low_stock:
#         print("No low-stock products.")
#         return

#     low_stock_products = (get_low_stock_products(products))

#     low_stock_products.sort(key=lambda product: product["quantity"])

#     print("LOW STOCK ")
#     print(f"Low-stock threshold: {LOW_STOCK_LEVEL}")
#     print()

#     for product in low_stock_products:

#         print(f"{product['product_id']} | "
#             f"{product['product_name']} | "
#             f"Stock: {product['quantity']}"
#         )

