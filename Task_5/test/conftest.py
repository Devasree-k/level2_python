import pytest

@pytest.fixture
def sample_products():
    return[ { "product_id": "P001", "product_name": "Laptop", "category": "Electronics", "price": 55000, "quantity": 5 },
            { "product_id": "P002", "product_name": "Mouse", "category": "Accessories", "price": 500, "quantity": 10 },
            { "product_id": "P003", "product_name": "Keyboard", "category": "Accessories", "price": 1500, "quantity": 25 } 
        ]