# from utils.common import read_products
from utils.common import Common

class Product:
    def __init__(self, common: Common):
        self.common = common

    def find_product(self, products: list[dict], product_id: str) -> dict | None:
        for product in products:
            if product["product_id"] == product_id:
                return product
        return None

    def view_products(self) -> None:
        products = self.common.read_products()
        if not products:
            print("No products available.")
            return

        print("PRODUCT LIST")
        print(f"{'ID':<8}{'Product':<18}{'Category':<15}{'Price':<12}{'Quantity':<10}")
        for product in products:
            print(f"{product['product_id']:<8}{product['product_name']:<18}{product['category']:<15}₹{product['price']:<11.2f}{product['quantity']:<10}")

    def display_product(self, product: dict) -> None:
        print("PRODUCT DETAILS")
        print(f"Product ID : {product['product_id']}")
        print(f"Name       : {product['product_name']}")
        print(f"Category   : {product['category']}")
        print(f"Price      : ₹{product['price']:.2f}")
        print(f"Quantity   : {product['quantity']}")

        # in this file want the folder structure to include exception, services, utilties, repositories and have the respective code in the proper file with correct naming for each file and dont change the functionality use the concepts i mentioned already  

