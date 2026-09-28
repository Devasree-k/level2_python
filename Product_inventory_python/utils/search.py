# from utils.common import read_products
# from utils.product import find_product


# def search_product() -> None:
#     products = read_products()

#     if not products:
#         print("No products available.")
#         return

#     product_id = input("Enter product ID: ").strip().upper()

#     product = find_product(products,product_id)

#     if product is None:
#         print("Product not found.")
#         return

#     print(" PRODUCT ")
#     print(f"ID       : {product['product_id']}")
#     print(f"Name     : {product['product_name']}")
#     print(f"Category : {product['category']}")
#     print(f"Price    : ₹{product['price']:.2f}")
#     print(f"Quantity : {product['quantity']}")



from utils.common import Common
from utils.product import Product


class Search:
    def __init__(self, common: Common, product: Product):
        self.common = common
        self.product = product

    def search_product(self) -> None:
        products = self.common.read_products()
        if not products:
            print("No products available.")
            return

        product_id = input("Enter product ID: ").strip().upper()
        selected_product = self.product.find_product(products, product_id)

        if selected_product is None:
            print("Product not found.")
            return

        self.product.display_product(selected_product)