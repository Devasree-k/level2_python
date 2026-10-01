
from utils.common import Common
from utils.product import Product
from dataclasses import dataclass

@dataclass
class Search:
    # def __init__(self, common: Common, product: Product):
    #     self.common = common
    #     self.product = product
    common:Common
    product:Product


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


        # product_model = self.convert_to_product_model(selected_product)
        # self.display_product(product_model)
        self.product.display_product(selected_product)