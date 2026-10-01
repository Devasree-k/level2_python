
from repositories.csv_repository import CSVRepository
from services.product_services import ProductService


def test_find_product(sample_products):
    repository = CSVRepository()
    product_service = ProductService(repository)

    result = product_service.find_product(sample_products, "P001")
    
    assert result is not None
    assert result["product_name"] == "Laptop"
    assert result["price"] == 55000


def test_product_not_found(sample_products):
    repository = CSVRepository()
    product_service = ProductService(repository)

    result = product_service.find_product(sample_products, "P999")

    assert result is None
