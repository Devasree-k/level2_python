from repositories.csv_repository import CSVRepository
from services.product_services import ProductService


class SearchService:

    def __init__(self, repository: CSVRepository, product: ProductService):
        self.repository = repository
        self.product = product

    def search_product(self) -> None:
        products = self.repository.read_products()

        if not products:
            print("No products available.")
            return

        product_id = input("Enter product ID: ").strip().upper()
        selected_product = self.product.find_product(products, product_id)

        if selected_product is None:
            print("Product not found.")
            return

        self.product.display_product(selected_product)

    def search_by_name(self) -> None:
        products = self.repository.read_products()
        if not products:
            print("No products available.")
            return
        name = input("Enter product name: ").strip().lower()

        results = [
            product for product in products
            if name in product["product_name"].lower()
        ]

        if not results:
            print("Product not found.")
            return

        print("SEARCH RESULTS")

        for product in results:
            self.product.display_product(product)