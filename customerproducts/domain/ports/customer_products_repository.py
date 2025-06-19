from abc import ABC, abstractmethod


class ICustomerProductsRepository(ABC):
    @abstractmethod
    def get_first_ten_products(self):
        pass

    def get_product_by_id(id: int):
        pass

    def get_categories_names(self):
        pass
