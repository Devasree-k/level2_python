from pydantic import BaseModel, Field


class Order(BaseModel):
    order_id: str = Field(min_length=1)
    product_id: str = Field(min_length=1)

    quantity: int = Field(gt=0)
    unit_price: float = Field(gt=0)
    total_amount: float = Field(gt=0)

    status: str = Field(min_length=1)