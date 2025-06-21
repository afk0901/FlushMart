from customerproducts.domain.customer_product import CustomerProduct
from customerproducts.application.product_services import GetProductList
from unittest.mock import Mock
from faker import Faker
import faker_commerce
import pytest


def make_fake_product(faker):
    return CustomerProduct(
        product_name=lambda: faker.ecommerce_name(),
        description=lambda: faker.text(max_nb_chars=10000),
        price=lambda: faker.pydecimal(left_digits=7, right_digits=2, positive=True),
    )


@pytest.fixture
def faker_instance():
    faker = Faker()
    faker.add_provider(faker_commerce.Provider)
    return faker


@pytest.fixture
def fake_products(faker_instance):
    return [make_fake_product(faker_instance) for _ in range(10)]


def test_return_list_of_products(fake_products):
    mock_repo = Mock()
    mock_repo.get_first_ten_products.return_value = fake_products

    service = GetProductList(mock_repo)
    result = service.execute()

    assert result == fake_products
