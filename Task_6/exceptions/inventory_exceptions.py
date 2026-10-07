class InventoryError(Exception):
    def __init__(self,message:str):
        self.message = message
        super().__init__(self.message)


class ProductNotFoundError(InventoryError):
    def __init__(self,product_id:str):
        message = f"Product with ID {product_id} is Not found. "
        super().__init__(message)



class InsufficientStockError(InventoryError):
    def __init__(self, available:int, requested :int):
        message = f"Insufficient Stock.  Available :{available} , Requested :{requested}"
        super().__init__(message)