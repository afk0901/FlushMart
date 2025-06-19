from customerproducts.infrastructure.models.customer_product_models import (
    CustomerProduct, CustomerProductCategory
)
from customerproducts.domain.ports.customer_products_repository import (
    ICustomerProductsRepository,
)
from customerproducts.domain.customer_product_entities import CustomerProductEntity, CustomerProductCategoryEntity


class SQLCustomerProductsRepository(ICustomerProductsRepository):
    # Implement pagination, first 10, then next 10 etc.
    def get_first_ten_products(self) -> list[CustomerProduct]:
        products = CustomerProduct.objects.all()[:10]
        # Consider a mapper
        return [
            CustomerProductEntity(
                product_name=customer_product.product_name,
                description=customer_product.description,
                price=customer_product.price
            )
            for customer_product in products
        ]

    def get_product_by_id(self, id: int) -> CustomerProductEntity:
        try:
            customer_product = CustomerProduct.objects.get(id=id)
            # Consider a mapper
            return CustomerProductEntity(
                product_name=customer_product.product_name,
                description=customer_product.description,
                price=customer_product.price,
            )
        except CustomerProduct.DoesNotExist:
            return CustomerProductEntity(product_name="", description="", price=0)
    
    # Strongly tied to product at the moment, so it stays here.
    def get_categories_names(self):
        categories = CustomerProductCategory.objects.all()
        return [CustomerProductCategoryEntity(name = category.name)
            for category in categories]

    def get_products_by_category(self):
        # Make a query filtered by category.
        ...
