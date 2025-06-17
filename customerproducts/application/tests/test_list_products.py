from unittest import TestCase
from customerproducts.domain.customer_product_entities import CustomerProductEntity
from faker import Faker
import faker_commerce
from unittest.mock import Mock
from customerproducts.application.product_services import GetProductList


class TestListProducts(TestCase):

    def setUp(self):

        faker = Faker()
        faker.add_provider(faker_commerce.Provider)

        customer_product_entitity0 = CustomerProductEntity(
            product_name=faker.ecommerce_name(),
            description=faker.text(max_nb_chars=10000),
            price=faker.pydecimal(left_digits=7, right_digits=2, positive=True),
        )

        customer_product_entitity1 = CustomerProductEntity(
            product_name=faker.ecommerce_name(),
            description=faker.text(max_nb_chars=10000),
            price=faker.pydecimal(left_digits=7, right_digits=2, positive=True),
        )

        customer_product_entitity2 = CustomerProductEntity(
            product_name=faker.ecommerce_name(),
            description=faker.text(max_nb_chars=10000),
            price=faker.pydecimal(left_digits=7, right_digits=2, positive=True),
        )

        self.repo_result = [
            customer_product_entitity0,
            customer_product_entitity1,
            customer_product_entitity2,
        ]

        self.expected_result = [customer_product_entitity0, customer_product_entitity1, customer_product_entitity2]

        self.mock_repo = Mock()
        self.mock_repo.get_first_ten_products.return_value = self.repo_result

    def test_return_list_of_products(self):
        get_product_list = GetProductList(self.mock_repo).execute()
        assert get_product_list == self.expected_result
