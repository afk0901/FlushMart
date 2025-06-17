from customerproducts.domain.ports.customer_products_repository import (
    ICustomerProductsRepository,
)


class GetProductList:

    def __init__(self, repo: ICustomerProductsRepository):
        self.repo = repo

    def execute(self):
        return self.repo.get_first_ten_products()


class GetProductById: ...


class GetProductListFilteredByCategory: ...
