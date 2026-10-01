import os
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()

DATA_DIR = Path("data")
PRODUCT_FILE = DATA_DIR/"products.json"
ORDER_FILE = DATA_DIR/"orders.json"

APP_NAME = os.getenv("APP_NAME", "Product Inventory System(Json). ")
LOW_STOCK_LEVEL = int(os.getenv("LOW_STOCK_LEVEL", "5"))
HIGH_STOCK_LEVEL = int(os.getenv("HIGH_STOCK_LEVEL", "20"))