
from utils.common import Common
from utils.product import Product
from utils.models import ProductModel

class Search:
    def __init__(self, common: Common, product: Product):
        self.common = common
        self.product = product

    def convert_to_product_model(self, product: dict) -> ProductModel:
        return ProductModel(
            product_id=product["product_id"],
            product_name=product["product_name"],
            category=product["category"],
            price=float(product["price"]),
            quantity=int(product["quantity"])
        )

    def display_product(self, product: ProductModel) -> None:
        print("PRODUCT DETAILS")
        print(f"Product ID : {product.product_id}")
        print(f"Name       : {product.product_name}")
        print(f"Category   : {product.category}")
        print(f"Price      : ₹{product.price:.2f}")
        print(f"Quantity   : {product.quantity}")


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


        product_model = self.convert_to_product_model(selected_product)
        self.display_product(product_model)
        # self.product.display_product(selected_product)