import os
import django
import random
from faker import Faker

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "flushmart.settings")
django.setup()

from customerproducts.infrastructure.models import (
    CustomerProduct,
    CustomerProductWarranty,
    CustomerProductCategory,
)
from datetime import datetime

fake = Faker()


def create_category():
    return CustomerProductCategory.objects.create(name=fake.word().capitalize())


def create_warranty():
    return CustomerProductWarranty.objects.create(
        warranty_start_date=datetime.now(), warranty_end_date=datetime.now()
    )


def run():
    categories = [create_category() for _ in range(3)]

    for _ in range(10):
        warranty = create_warranty()
        category = random.choice(categories)

        CustomerProduct.objects.create(
            warranty=warranty,
            category=category,
            product_name=fake.word().capitalize(),
            description=fake.text(max_nb_chars=200),
            price=round(random.uniform(10, 5000), 2),
            image="customer_products_images/dummy.jpg",
        )

    print("CustomerProducts populated.")


if __name__ == "__main__":
    run()
