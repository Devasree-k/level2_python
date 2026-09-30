import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

DATA_DIR = Path("data")
REPORT_DIR = Path("reports")

PRODUCT_FILE = DATA_DIR / "product.csv"
ORDER_FILE = DATA_DIR / "orders.csv"

REPORT_FILE = REPORT_DIR / "inventory_report.txt"

APP_NAME = os.getenv("APP_NAME","Product Inventory System")

LOW_STOCK_LEVEL = int(os.getenv("LOW_STOCK_LEVEL","5"))

