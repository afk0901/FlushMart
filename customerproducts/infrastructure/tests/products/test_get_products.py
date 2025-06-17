from django.test import TestCase
from customerproducts.infrastructure.customer_products_repository import SQLCustomerProductsRepository
from model_bakery import baker
from model_bakery.recipe import Recipe
from customerproducts.domain.entities.customer_product_entity import CustomerProductEntity
from faker import Faker
import faker_commerce

class TestGetProducts(TestCase):

    @classmethod
    def setUpTestData(cls):
        faker = Faker()
        faker.add_provider(faker_commerce.Provider)

        cls.customer_product_recipe = Recipe(
            'CustomerProduct',
            product_name = lambda: faker.ecommerce_name(),
            description =  lambda: faker.text(max_nb_chars=10000),
            price = lambda: faker.pydecimal(left_digits=7, right_digits=2, 
                                            positive=True)
        )
        
    def test_get_first_ten_product_successfully(self):
        self.customer_product_recipe.make(_quantity=11)
        products = SQLCustomerProductsRepository().get_products()
        assert len(products) == 10

        # Randomly sampling the returned list

        customer_product_entitity0 = CustomerProductEntity(
            product_name=products[0].product_name,
            description=products[0].description,
            price=products[0].price
        )

        customer_product_entitity3 = CustomerProductEntity(
            product_name=products[3].product_name,
            description=products[3].description,
            price=products[3].price
        )

        customer_product_entitity9 = CustomerProductEntity(
            product_name=products[9].product_name,
            description=products[9].description,
            price=products[9].price
        )

        assert products[0] == customer_product_entitity0
        assert products[3] == customer_product_entitity3
        assert products[9] == customer_product_entitity9

    def test_get_products_when_no_products_exist(self):
         products = SQLCustomerProductsRepository().get_products()
         assert len(products) == 0

    def test_get_product_by_id_successfully(self):
        single_customer_product = self.customer_product_recipe.make(id=3)
        # Making few ones because to be more sure of it's looking by correct id.
        baker.make("CustomerProduct", id=5)
        baker.make("CustomerProduct", id=1)

        customer_product_entitity = CustomerProductEntity(
            title=single_customer_product.product_name,
            description=single_customer_product.description,
            price=single_customer_product.price
        )
        products = SQLCustomerProductsRepository().get_product_by_id(3)
        assert products == customer_product_entitity
    
    def test_product_by_id_does_not_exist(self):
        baker.make("CustomerProduct", id=5)
        baker.make("CustomerProduct", id=1)
        product = SQLCustomerProductsRepository().get_product_by_id(3)
        empty_customer_product_entitity = CustomerProductEntity(
            product_name="",
            description="",
            price=0
        )
        assert product == empty_customer_product_entitity