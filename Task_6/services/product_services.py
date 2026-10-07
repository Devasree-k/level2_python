from repositories.json_repository import JSONRepository
import asyncio
from models.product_model import Product
from exceptions.inventory_exceptions import ProductNotFoundError

class ProductService:

    def __init__(self, repository: JSONRepository):
        self.repository = repository

    def find_product(self, products: list[Product], product_id: str) -> Product:
        product = next(
            (product for product in products
             if product.product_id == product_id),
            None
        )
    
        if product is None:
            raise ProductNotFoundError(product_id)

        return product


    def display_product(self, product: Product) -> None:
        print("PRODUCT DETAILS")
        print(f"Product ID : {product.product_id}")
        print(f"Name       : {product.product_name}")
        print(f"Category   : {product.category}")
        print(f"Price      : {product.price}")
        print(f"Quantity   : {product.quantity}")

    async def view_products(self) -> None:
        products = await self.repository.read_products()

        if not products:
            print("No products available.")
            return

        print("PRODUCT LIST")
        print(f"{'ID':<8}{'Product':<18}{'Category':<15}{'Price':<12}{'Quantity':<10}")

        for product in products:
            print(
                f"{product.product_id:<8}"
                f"{product.product_name:<18}"
                f"{product.category:<15}"
                f"₹{product.price:<11.2f}"
                f"{product.quantity:<10}"
            )