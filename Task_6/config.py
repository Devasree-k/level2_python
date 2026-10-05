# # import os
# # from dotenv import load_dotenv
# # from pathlib import Path

# # load_dotenv()

# # DATA_DIR = Path("data")

# # REPORT_DIR = Path("reports")
# # PRODUCT_FILE = DATA_DIR/"products.json"
# # ORDER_FILE = DATA_DIR/"orders.json"

# # REPORT_FILE = REPORT_DIR / "inventory_report.txt"

# # APP_NAME = os.getenv("APP_NAME", "Product Inventory System(Json). ")
# # LOW_STOCK_LEVEL = int(os.getenv("LOW_STOCK_LEVEL", "5"))
# # HIGH_STOCK_LEVEL = int(os.getenv("HIGH_STOCK_LEVEL", "20"))


# import os
# from pathlib import Path
# from dotenv import load_dotenv

# load_dotenv()

# DATA_DIR = Path("data")
# REPORT_DIR = Path("reports")

# PRODUCT_FILE = DATA_DIR / "product.csv"
# ORDER_FILE = DATA_DIR / "orders.csv"
# REPORT_FILE = REPORT_DIR / "inventory_report.txt"

# APP_NAME = os.getenv("APP_NAME", "Product Inventory System")
# LOW_STOCK_LEVEL = int(os.getenv("LOW_STOCK_LEVEL", "5"))
# HIGH_STOCK_LEVEL = int(os.getenv("HIGH_STOCK_LEVEL", "20"))



import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent

DATA_DIR = BASE_DIR / "data"
REPORT_DIR = BASE_DIR / "reports"

PRODUCT_FILE = DATA_DIR / "products.json"
ORDER_FILE = DATA_DIR / "orders.json"
REPORT_FILE = REPORT_DIR / "inventory_report.txt"

APP_NAME = os.getenv("APP_NAME", "Project Inventory Using Json")

LOW_STOCK_LEVEL = int(os.getenv("LOW_STOCK_LEVEL", "5"))
HIGH_STOCK_LEVEL = int(os.getenv("HIGH_STOCK_LEVEL", "20"))