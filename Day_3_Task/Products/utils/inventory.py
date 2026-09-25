import csv
from pathlib import Path

Product_file = Path("data/product.csv")
Stock_file = Path("data/stock.csv")


def read_products():
    products = []
    with open(Product_file,"r") as file:
        reader = csv.DictReader(file)
        for data in reader:
            data["price"] = float(data["price"])
            products.append(data)

    return products

def read_stock():
    stock = []
    with open(Stock_file,"r") as  file:
        reader = csv.DictReader(file)
        for data in reader:
            data["quantity"] = int(data["quantity"])
            data["total_value"] = float(data["total_value"])

            stock.append(data)

    return stock

def write_stock(stock):
    field_name = [
        "product_id",
        "quantity",
        "total_value",
        "status"
    ]

    with open(Stock_file,"w")as file:
        writer = csv.DictWriter(file,fieldnames=field_name)
        writer.writeheader()
        writer.writerows(stock)
