from repositories.csv_repository import CSVRepository
from services.product_services import ProductService


class OrderService:

    def __init__(self, repository: CSVRepository, product: ProductService):
        self.repository = repository
        self.product = product

    def generate_order_id(self, orders: list[dict]) -> str:
        numbers = [
            int(order["order_id"][1:])
            for order in orders
            if order["order_id"][1:].isdigit()
        ]

        return f"O{max(numbers, default=0) + 1:03d}"

    def calculate_order_amount(self, price: float, quantity: int) -> float:
        return price * quantity

    def validate_order(self, product: dict, quantity: int) -> bool:
        return all([
            quantity > 0,
            quantity <= product["quantity"],
            product["price"] > 0
        ])

    def place_order(self) -> None:
        products = self.repository.read_products()
        orders = self.repository.read_orders()

        if not products:
            print("No products available.")
            return

        product_id = input("Enter product ID: ").strip().upper()

        try:
            quantity = int(input("Enter quantity: "))
        except ValueError:
            print("Quantity must be a valid number.")
            return

        selected_product = self.product.find_product(products, product_id)

        if selected_product is None:
            print("Product not found.")
            return

        if not self.validate_order(selected_product, quantity):
            if quantity <= 0:
                print("Quantity must be greater than zero.")
            elif quantity > selected_product["quantity"]:
                print(f"Insufficient stock. Available: {selected_product['quantity']}")
            else:
                print("Product price is invalid.")
            return

        total_amount = self.calculate_order_amount(
            selected_product["price"], quantity
        )

        order_id = self.generate_order_id(orders)

        order = {
            "order_id": order_id,
            "product_id": selected_product["product_id"],
            "quantity": quantity,
            "unit_price": selected_product["price"],
            "total_amount": total_amount,
            "status": "Completed"
        }

        selected_product["quantity"] -= quantity
        orders.append(order)

        self.repository.write_products(products)
        self.repository.write_orders(orders)

        print("ORDER SUCCESS")
        print(f"Order ID        : {order_id}")
        print(f"Product         : {selected_product['product_name']}")
        print(f"Quantity        : {quantity}")
        print(f"Unit Price      : ₹{selected_product['price']:.2f}")
        print(f"Total Amount    : ₹{total_amount:.2f}")
        print(f"Remaining Stock : {selected_product['quantity']}")
        print("Status          : Completed")

    def view_orders(self) -> None:
        orders = self.repository.read_orders()

        if not orders:
            print("No orders available.")
            return

        print("ORDER HISTORY")
        print(f"{'Order ID':<10}{'Product':<10}{'Quantity':<10}{'Price':<14}{'Amount':<14}{'Status':<12}")

        for order in orders:
            print(
                f"{order['order_id']:<10}"
                f"{order['product_id']:<10}"
                f"{order['quantity']:<10}"
                f"₹{order['unit_price']:<13.2f}"
                f"₹{order['total_amount']:<13.2f}"
                f"{order['status']:<12}"
            )

