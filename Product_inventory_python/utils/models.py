from dataclasses import dataclass


@dataclass
class ProductModel:
    product_id: str
    product_name: str
    category: str
    price: float
    quantity: int