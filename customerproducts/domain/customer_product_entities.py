from dataclasses import dataclass


@dataclass
class CustomerProductEntity:
    product_name: str
    description: str
    price: float
