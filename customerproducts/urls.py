from django.urls import path
from customerproducts.presentation.views.product_list_view import ProductListView

urlpatterns = [path("", ProductListView.as_view(), name="product-list")]
