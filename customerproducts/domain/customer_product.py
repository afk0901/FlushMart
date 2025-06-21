from dataclasses import dataclass


@dataclass
class CustomerProduct:
    product_name: str = ""
    description: str = ""
    price: float = 0
    image_url: str = ""

@dataclass
class CustomerProductCategory:
    name: str = ""
