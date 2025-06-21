from dataclasses import dataclass


@dataclass
class CustomerProduct:
    product_name: str
    description: str
    price: float

@dataclass
class CustomerProductCategory:
    name: str
