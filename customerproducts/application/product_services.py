from customerproducts.domain.ports.customer_products_repository import ICustomerProductsRepository

class ListProductsService:

    def __init__(self, repo : ICustomerProductsRepository):
        self.repo = repo
