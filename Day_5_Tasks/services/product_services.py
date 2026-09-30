from repositories.csv_repository import CSVRepository


class ProductService:

    def __init__(self, repository: CSVRepository):
        self.repository = repository

    def find_product(self, products: list[dict], product_id: str) -> dict | None:
        return next(
            (product for product in products
             if product["product_id"] == product_id),
            None
        )

    def display_product(self, product: dict) -> None:
        print("PRODUCT DETAILS")
        print(f"Product ID : {product['product_id']}")
        print(f"Name       : {product['product_name']}")
        print(f"Category   : {product['category']}")
        print(f"Price      : ₹{product['price']:.2f}")
        print(f"Quantity   : {product['quantity']}")

    def view_products(self) -> None:
        products = self.repository.read_products()

        if not products:
            print("No products available.")
            return

        print("PRODUCT LIST")
        print(f"{'ID':<8}{'Product':<18}{'Category':<15}{'Price':<12}{'Quantity':<10}")

        for product in products:
            print(
                f"{product['product_id']:<8}"
                f"{product['product_name']:<18}"
                f"{product['category']:<15}"
                f"₹{product['price']:<11.2f}"
                f"{product['quantity']:<10}"
            )