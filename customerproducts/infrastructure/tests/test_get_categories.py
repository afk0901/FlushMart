from faker import Faker
import faker_commerce
from django.test import TestCase
from customerproducts.infrastructure.customer_products_repository import (
    SQLCustomerProductsRepository,
)
from model_bakery.recipe import Recipe
from customerproducts. domain.customer_product_entities import CustomerProductCategoryEntity
from model_bakery import baker


class TestGetCategories(TestCase):

    @classmethod
    def setUpTestData(cls):
        faker = Faker()
        faker.add_provider(faker_commerce.Provider)

        cls.categories_recipe = Recipe(
            "CustomerProductCategory",
            name=lambda: faker.text(max_nb_chars=100)
        )

    def assert_entity_equal(self, product_model, entity):
        assert entity == CustomerProductCategoryEntity(name=product_model.name)

    def test_get_categories_names(self):
        expected_categories_from_db = self.categories_recipe.make(_quantity=5)
        categories = SQLCustomerProductsRepository().get_categories_names()
        assert len(categories) == 5

        # Randomly sampling the returned list
        self.assert_entity_equal(product_model=expected_categories_from_db[0], entity=categories[0])
        self.assert_entity_equal(product_model=expected_categories_from_db[1], entity=categories[1])
        self.assert_entity_equal(product_model=expected_categories_from_db[2], entity=categories[2])
