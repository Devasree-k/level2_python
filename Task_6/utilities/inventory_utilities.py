from config import LOW_STOCK_LEVEL, HIGH_STOCK_LEVEL

from models.product_model import Product


def get_low_stock_products(products: list[Product]) -> list[Product]:
    # return [
    #     product for product in products
    #     if product["quantity"] <= LOW_STOCK_LEVEL
    # ]
    return list(
        filter(
            lambda product: product.quantity <= LOW_STOCK_LEVEL,
            products
        )
    )


def get_high_stock_products(products: list[Product]) -> list[Product]:
    return [
        product
        for product in products
        if product.quantity >= HIGH_STOCK_LEVEL
    ]