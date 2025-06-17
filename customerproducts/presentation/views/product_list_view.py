from django.views.generic import TemplateView
from customerproducts.application.product_services import GetProductList
from customerproducts.infrastructure.customer_products_repository import (
    SQLCustomerProductsRepository,
)


class ProductListView(TemplateView):
    template_name = "product_list.html"

    product_list_service = GetProductList(SQLCustomerProductsRepository())
    products = product_list_service.execute()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["products"] = [
            {
                "product_name": product.product_name,
                "description": product.description,
                "price": product.price,
            }
            for product in self.products
        ]
        return context
