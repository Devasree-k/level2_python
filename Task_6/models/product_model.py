from pydantic import BaseModel, Field

class Product(BaseModel):
    product_id :str = Field(min_length=1)
    product_name : str = Field(min_length = 1)
    category: str = Field(min_length=1)
    price : float = Field(gt=0)
    quantity :int = Field(ge=0)


