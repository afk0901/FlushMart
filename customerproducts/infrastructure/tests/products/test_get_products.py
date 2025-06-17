from django.test import TestCase
from customerproducts.infrastructure.customer_products_repository import (
    SQLCustomerProductsRepository,
)
from model_bakery import baker
from model_bakery.recipe import Recipe
from customerproducts.domain.customer_product_entities import CustomerProductEntity
from faker import Faker
import faker_commerce


class TestGetProducts(TestCase):

    @classmethod
    def setUpTestData(cls):
        faker = Faker()
        faker.add_provider(faker_commerce.Provider)

        cls.customer_product_recipe = Recipe(
            "CustomerProduct",
            product_name=lambda: faker.ecommerce_name(),
            description=lambda: faker.text(max_nb_chars=10000),
            price=lambda: faker.pydecimal(left_digits=7, right_digits=2, positive=True),
        )

    def assert_entity_equal(self, product_model, entity):
        assert entity == CustomerProductEntity(
            product_name=product_model.product_name,
            description=product_model.description,
            price=product_model.price,
        )

    def test_get_first_ten_product_successfully(self):
        self.customer_product_recipe.make(_quantity=11)
        products = SQLCustomerProductsRepository().get_first_ten_products()
        assert len(products) == 10

        # Randomly sampling the returned list
        self.assert_entity_equal(product_model=products[0], entity=products[0])
        self.assert_entity_equal(product_model=products[3], entity=products[3])
        self.assert_entity_equal(product_model=products[9], entity=products[9])

    def test_get_products_when_no_products_exist(self):
        products = SQLCustomerProductsRepository().get_first_ten_products()
        assert len(products) == 0

    def test_get_product_by_id_successfully(self):
        expected_product = self.customer_product_recipe.make(id=3)
        # Making few ones because to be more sure of it's looking by correct id.
        baker.make("CustomerProduct", id=5)
        baker.make("CustomerProduct", id=1)

        result = SQLCustomerProductsRepository().get_product_by_id(3)
        self.assert_entity_equal(product_model=expected_product, entity=result)

    def test_product_by_id_does_not_exist(self):
        baker.make("CustomerProduct", id=5)
        baker.make("CustomerProduct", id=1)
        result = SQLCustomerProductsRepository().get_product_by_id(99)
        assert result == CustomerProductEntity(product_name="", description="", price=0)
