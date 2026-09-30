from utils.common import Common
from utils.product import Product

class Order:
    def __init__(self,common:Common, product:Product):
        self.common = common
        self.product = product

    def generate_order_id(self, orders: list[dict]) -> str:
        if not orders:
            return "O001"

        order_numbers = []
        for order in orders:
            try:
                number = int(order["order_id"][1:])
                order_numbers.append(number)
            except (ValueError, IndexError):
                continue

        if not order_numbers:
            return "O001"

        next_number = max(order_numbers) + 1
        return f"O{next_number:03d}"

    def calculate_order_amount(self, price: float, quantity: int) -> float:
        return price * quantity

    def validate_order(self, product: dict, quantity: int) -> bool:
        conditions = [
            quantity > 0,
            quantity <= product["quantity"],
            product["price"] > 0
        ]
        return all(conditions)

    def place_order(self) -> None:
        products = self.common.read_products()
        orders = self.common.read_orders()

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
            elif selected_product["price"] <= 0:
                print("Product price is invalid.")
            return

        total_amount = self.calculate_order_amount(selected_product["price"], quantity)
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

        self.common.write_products(products)
        self.common.write_orders(orders)

        print("ORDER SUCCESS")
        print(f"Order ID        : {order_id}")
        print(f"Product         : {selected_product['product_name']}")
        print(f"Quantity        : {quantity}")
        print(f"Unit Price      : ₹{selected_product['price']:.2f}")
        print(f"Total Amount    : ₹{total_amount:.2f}")
        print(f"Remaining Stock : {selected_product['quantity']}")
        print("Status          : Completed")

    def view_orders(self) -> None:
        orders = self.common.read_orders()
        if not orders:
            print("No orders available.")
            return

        print("ORDER HISTORY")
        print(f"{'Order ID':<10}{'Product':<10}{'Quantity':<10}{'Price':<14}{'Amount':<14}{'Status':<12}")

        for order in orders:
            print(f"{order['order_id']:<10}{order['product_id']:<10}{order['quantity']:<10}₹{order['unit_price']:<13.2f}₹{order['total_amount']:<13.2f}{order['status']:<12}")