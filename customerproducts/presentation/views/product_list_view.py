from django.views.generic import TemplateView
from customerproducts.application.product_services import GetProductList
from customerproducts.infrastructure.customer_products_repository import (
    SQLCustomerProductsRepository
)


class ProductListView(TemplateView):
    template_name = "product_list.html"

    product_list_service = GetProductList(SQLCustomerProductsRepository())

    def get_context_data(self, **kwargs):
        products = self.product_list_service.execute()
        context = super().get_context_data(**kwargs)

        context["products"] = [
            {
                "product_name": product.product_name,
                "description": product.description,
                "price": product.price,
                "image_url" : product.image_url if product.image_url else "customer_products_images/placeholder.jpg"
            }
            for product in products
        ]
        return context
