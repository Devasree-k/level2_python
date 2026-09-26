from .inventory import read_stock


def check_low_stock():
    stock = read_stock()
    if not stock:
        print("No stock records available.")
        return
    found = False

    print("LOW STOCK PRODUCTS")
    
    print(
        f"{'ID':<10}"
        f"{'QUANTITY':<12}"
        f"{'STATUS':<12}"
    )


    for item in stock:
        if item["status"] == "Low Stock":
            found = True
            print(
                f"{item['product_id']:<10}"
                f"{item['quantity']:<12}"
                f"{item['status']:<12}"
            )

    if not found:
        print("No low-stock products.")


