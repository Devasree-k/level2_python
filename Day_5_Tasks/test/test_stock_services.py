from utilities.inventory_utilities import (
    get_high_stock_products,
    get_low_stock_products
)

def test_get_high_stock_products(sample_products):
    result = get_high_stock_products(sample_products)

    assert len(result) == 1
    assert result[0]["product_id"] == "P003"

def test_get_low_stock_products(sample_products):
    result = get_low_stock_products(sample_products)
    assert len(result) == 1
    assert result[0]["product_id"] == "P001"