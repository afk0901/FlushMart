from django.test import TestCase
from customerproducts.infrastructure.customer_products_repository import (
    SQLCustomerProductsRepository,
)
from model_bakery import baker
from customerproducts.domain.customer_product import CustomerProduct
from product_mocks import mock_product

class TestGetProducts(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.product = mock_product()

    def assert_entity_equal(self, product_model, entity):
        assert entity == CustomerProduct(
            product_name=product_model.product_name,
            description=product_model.description,
            price=product_model.price,
            image_url= product_model.image
        )

    def test_get_first_ten_product_successfully(self):
        expected_products_from_db = self.product.make(_quantity=11)
        products = SQLCustomerProductsRepository().get_first_ten_products()
        assert len(products) == 10

        # Randomly sampling the returned list
        self.assert_entity_equal(product_model=expected_products_from_db[0], entity=products[0])
        self.assert_entity_equal(product_model=expected_products_from_db[3], entity=products[3])
        self.assert_entity_equal(product_model=expected_products_from_db[9], entity=products[9])

    def test_get_products_when_no_products_exist(self):
        products = SQLCustomerProductsRepository().get_first_ten_products()
        assert len(products) == 0

    def test_get_product_by_id_successfully(self):
        expected_product = self.product.make(id=3)
        # Making few ones because to be more sure of it's looking by correct id.
        baker.make("CustomerProductModel", id=5)
        baker.make("CustomerProductModel", id=1)

        result = SQLCustomerProductsRepository().get_product_by_id(3)
        self.assert_entity_equal(product_model=expected_product, entity=result)

    def test_product_by_id_does_not_exist(self):
        baker.make("CustomerProductModel", id=5)
        baker.make("CustomerProductModel", id=1)
        result = SQLCustomerProductsRepository().get_product_by_id(99)
        assert result == CustomerProduct()
        