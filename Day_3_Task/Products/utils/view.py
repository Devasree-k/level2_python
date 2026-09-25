
from .inventory import (
    read_products,
    read_stock
    # write_stock
)

def view_products():
    products = read_products()

    if not products:
        print("No products available")
        return

    print("Products")
    print(
        f"{'ID':<8}"
        f"{'NAME':<15}"
        f"{'CATEGORY':<15}"
        f"{'PRICE':<10}"
    )

    for product in products:

        print(
            f"{product['product_id']:<8}"
            f"{product['product_name']:<15}"
            f"{product['category']:<15}"
            f"{product['price']:<10}"
        )


def view_stock():

    stock = read_stock()
    products = read_products()

    product_display = {
        product["product_id"]: product
        for product in products
    }

    if not stock:
        print("No stock records available.")
        return

    print("STOCK")

    print(
        f"{'ID':<8}"
        f"{'PRODUCT':<15}"
        f"{'QTY':<8}"
        f"{'VALUE':<12}"
        f"{'STATUS':<12}"
    )


    for item in stock:
        product = product_display.get(item["product_id"])
        product_name = (
            product["product_name"]
            if product
            else "Unknown"
        )

        print(
            f"{item['product_id']:<8}"
            f"{product_name:<15}"
            f"{item['quantity']:<8}"
            f"{item['total_value']:<12.2f}"
            f"{item['status']:<12}"
        )
