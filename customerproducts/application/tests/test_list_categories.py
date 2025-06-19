from customerproducts.domain.customer_product_entities import CustomerProductCategoryEntity
from customerproducts.application.product_services import GetProductCategories
from unittest.mock import Mock
from faker import Faker
import faker_commerce
import pytest


def make_fake_category(faker):
    return CustomerProductCategoryEntity(
        name=lambda: faker.text(max_nb_chars=100)
    )


@pytest.fixture
def faker_instance():
    faker = Faker()
    faker.add_provider(faker_commerce.Provider)
    return faker


@pytest.fixture
def fake_categories(faker_instance):
    return [make_fake_category(faker_instance) for _ in range(10)]


def test_return_list_of_categories(fake_categories):
    mock_repo = Mock()
    mock_repo.get_categories_names.return_value = fake_categories

    service = GetProductCategories(mock_repo)
    result = service.execute()
    assert result == fake_categories
