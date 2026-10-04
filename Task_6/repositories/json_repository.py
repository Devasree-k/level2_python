import json
from config import PRODUCT_FILE, ORDER_FILE

class JSONRepository:
    def read_products(self)->list[dict]:
        try:
            with open(PRODUCT_FILE,"r")as file:
                return json.load(file)
        except FileNotFoundError:
            print("Product file not found")

    def write_products(self, products:list[dict])->None:
        with open(PRODUCT_FILE,"w")as file:
            json.dump(products,file,indent=4)

    def read_orders(self)->list[dict]:
        try:
            with open(ORDER_FILE,"r")as file:
                return json.load(file)
        except FileNotFoundError:
            print("Product file not found")

    def write_orders(self, orders:list[dict])->None:
        with open(PRODUCT_FILE,"w")as file:
            json.dump(orders,file,indent=4)

        