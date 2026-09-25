
from .inventory import(
    read_stock,
    read_products,
    write_stock
)

def update_stock():
    products = read_products()
    stock = read_stock()

    product_id=input("Enter the Product ID to update : ").upper()
    product = None
    for p in products:
        if p["product_id"] == product_id:
            product = p
            break
    if product is None:
        print("Product doesn't exist")
        return


    stock_record = None
    for s in stock:
        if s["product_id"]==product_id:
            stock_record = s
            break
    if stock_record is None:
        print("Stock record doesn't exist.")


    try:

        quantity = int(
            input("Enter new quantity: ")
        )

        if quantity < 0:
            print("Quantity cannot be negative.")
            return

        # Update values
        stock_record["quantity"] = quantity

        # Recalculate total value
        stock_record["total_value"] = (
            quantity * product["price"]
        )

        # Recalculate status
        if quantity <= 5:
            stock_record["status"] = "Low Stock"
        else:
            stock_record["status"] = "Available"

        write_stock(stock)
        print("Stock updated successfully.")

    except ValueError:
        print("Invalid input.")

