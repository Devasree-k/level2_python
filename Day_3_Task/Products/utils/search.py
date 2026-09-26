from .common import (
    read_products,
    read_stock
)

def search_product():

    products = read_products()
    stock = read_stock()

    product_id = input("Enter product ID to search: ").strip().upper()
    product = None
    for p in products:
        if p["product_id"] == product_id:
            product = p
            break

    if product is None:
        print("Product does not exist.")
        return

    print("PRODUCT")
    print(f"Product ID : {product['product_id']}")
    print(f"Name       : {product['product_name']}")
    print(f"Category   : {product['category']}")
    print(f"Price      : ₹{product['price']:.2f}")

    # Find stock information
    stock_record = None
    for item in stock:
        if item["product_id"] == product_id:
            stock_record = item
            break

    if stock_record is not None:
        print( f"Quantity   : {stock_record['quantity']}")
        print(f"Value      : ₹{stock_record['total_value']:.2f}")
        print( f"Status     : {stock_record['status']}" )

    else:
        print("Stock       : No stock record")