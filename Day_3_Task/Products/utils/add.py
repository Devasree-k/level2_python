from .inventory import (
    read_stock,
    read_products,
    write_stock
)



def add_stock():

    products = read_products()
    stock = read_stock()

    product_id = input("Enter product ID: ").strip().upper()

    # Check whether product exists
    product = None
    for p in products:
        if p["product_id"] == product_id:
            product = p
            break

    if product is None:
        print(f"Product {product_id} does not exist in products.csv.")
    else:
        print(product)

    # Check whether stock record already exists
    existing = None
    for items in stock:
        if items["product_id"] == product_id:
            existing = items
            break

    if existing is not None:
        print("Stock record already exists. Use Update instead.")
        return

    try:
        quantity = int(input("Enter quantity: "))

        if quantity < 0:
            print("Quantity cannot be negative.")
            return

        total_value = quantity * product["price"]
        if quantity <= 5:
            status = "Low Stock"
        else:
            status = "Available"

        new_record = {
            "product_id": product_id,
            "quantity": quantity,
            "total_value": total_value,
            "status": status
        }

        stock.append(new_record)
        write_stock(stock)
        print("Stock record added successfully.")

    except ValueError:
        print("Invalid input. ")
