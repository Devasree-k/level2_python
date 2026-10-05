from repositories.json_repository import JSONRepository


class ProductDetailService:

    def __init__(self, repository: JSONRepository):
        self.repository = repository

    async def display_product_details(self) -> None:
        products = await self.repository.read_products()
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

            product_id = product.product_id
            price = product.price

            sold = sum(
                order.quantity
                for order in orders
                if order.product_id == product_id
            )

            # remaining = product["quantity"]
            # opening_stock = remaining + sold
            # sales_revenue = price * sold
            # stock_value = price * remaining

            remaining = product.quantity
            opening_stock = remaining + sold
            sales_revenue = product.price * sold
            stock_value = product.price * remaining

            print(
                f"{product.product_name:<12}"
                f"{product.category:<15}"
                f"₹{price:<10}"
                f"{opening_stock:<11}"
                f"{sold:<8}"
                f"{remaining:<12}"
                f"₹{sales_revenue:<13}"
                f"₹{stock_value:<13}"
            )