from abc import ABC, abstractmethod

class ICustomerProductsRepository(ABC):
    @abstractmethod
    def get_products(self):
        pass
    def get_product_by_id(id: int):
        pass