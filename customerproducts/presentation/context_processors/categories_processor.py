from customerproducts.infrastructure.customer_products_repository import (
    SQLCustomerProductsRepository,
)
from customerproducts.application.product_services import GetProductCategories

product_categories_service = GetProductCategories(SQLCustomerProductsRepository())

def categories_processor(request):
    categories = product_categories_service.execute()
    return {"categories": [
            {
                "category_name": category.name,
            }
            for category in categories
        ]}
    