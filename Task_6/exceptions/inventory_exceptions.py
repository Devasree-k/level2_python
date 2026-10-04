class InventoryError(Exception):
    pass


class ProductNotFoundError(InventoryError):
    pass


class InsufficientStockError(InventoryError):
    pass