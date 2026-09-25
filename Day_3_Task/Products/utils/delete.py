from .inventory import(
    # read_products,
    read_stock,
    write_stock
)


def delete_stock():
    stock = read_stock()

    product_id = input("Enter product ID to delete : ").upper()
    stock_record = None
    for s in stock:
        if s["product_id"]==product_id:
            stock_record = s

    if stock_record is None:
        print("Stock record does not exist.")
        return

    stock.remove(stock_record)
    write_stock(stock)

    print(f"Stock record for {product_id} deleted successfully.")




