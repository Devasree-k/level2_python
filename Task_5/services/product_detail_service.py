from repositories.csv_repository import CSVRepository

class ProductDetailService:
    def __init__(self,repository : CSVRepository):
        self.repository = repository

    def display_product_details(self)->None:
        products = self.repository.read_products()
        orders = self.repository.read_orders()

        if not products:
            print("No products available")
            return

        print("\n PRODUCT DETAILS\n")

        print(
            f"{'Product':<12}"
            f"{'Category':<15}"
            f"{'Price':<10}"
            f"{'Opening':<11}"
            f"{'Sold':<8}"
            f"{'Remaining':<12}"
            f"{'Sales':<14}"
            f"{'Stock Value':<14}"
        )

        for product in products:

            product_id = product["product_id"]
            price = product["price"]
            opening_stock = product["quantity"]

            sold = sum(
                order["quantity"]
                for order in orders
                if order["product_id"] == product_id
            )

            remaining = opening_stock - sold

            sales_revenue = price * sold

            stock_value = price * remaining

            print(
                f"{product['product_name']:<12}"
                f"{product['category']:<15}"
                f"₹{price:<10}"
                f"{opening_stock:<11}"
                f"{sold:<8}"
                f"{remaining:<12}"
                f"₹{sales_revenue:<13}"
                f"₹{stock_value:<13}"
            )





