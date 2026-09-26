import csv
from pathlib import Path
import os 
from dotenv import load_dotenv

Product_file = Path("data/product.csv")
Stock_file = Path("data/stock.csv")

load_dotenv()
APP_NAME = os.getenv("APP_NAME","Products Inventory")

def read_products()->list[dict]:    
    products = []
    try:

        with open(Product_file,"r") as file:
            reader = csv.DictReader(file)
            for data in reader:
                data["price"] = float(data["price"])
                products.append(data)

    except FileNotFoundError:
        print("Product file not found.")

    except ValueError:
        print("Invalid price value in product.csv.")

    return products

def read_stock()->list[dict]:
    stock = []
    try:

        with open(Stock_file,"r") as  file:
            reader = csv.DictReader(file)
            for data in reader:
                data["quantity"] = int(data["quantity"])
                data["total_value"] = float(data["total_value"])

                stock.append(data)

    except FileNotFoundError:
        print("Stock file not found.")

    except ValueError:
        print("Invalid numeric value in stock.csv.")

    return stock

def write_stock(stock:list[dict])->None:
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

