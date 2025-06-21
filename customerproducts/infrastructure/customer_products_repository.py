from customerproducts.infrastructure.models.customer_product_models import (
    CustomerProductModel, CustomerProductCategoryModel
)
from customerproducts.domain.ports.customer_products_repository import (
    ICustomerProductsRepository,
)
from customerproducts.domain.customer_product import CustomerProduct, CustomerProductCategory


class SQLCustomerProductsRepository(ICustomerProductsRepository):
    # Implement pagination, first 10, then next 10 etc.
    def get_first_ten_products(self) -> list[CustomerProduct]:
        products = CustomerProductModel.objects.all()[:10]
        # Consider a mapper
        return [
            CustomerProduct(
                product_name=customer_product.product_name,
                description=customer_product.description,
                price=customer_product.price,
                image_url=customer_product.image
            )
            for customer_product in products
        ]

    def get_product_by_id(self, id: int) -> CustomerProduct:
        try:
            customer_product = CustomerProductModel.objects.get(id=id)
            # Consider a mapper
            return CustomerProduct(
                product_name=customer_product.product_name,
                description=customer_product.description,
                price=customer_product.price,
                image_url=customer_product.image
            )
        except CustomerProductModel.DoesNotExist:
            return CustomerProduct()
    
    # Strongly tied to product at the moment, so it stays here.
    def get_categories_names(self):
        categories = CustomerProductCategoryModel.objects.all()
        return [CustomerProductCategory(name = category.name)
            for category in categories]

    def get_products_by_category(self):
        # Make a query filtered by category.
        ...
