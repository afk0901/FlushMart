# Quick and dirty way to populate products in the database as we don't have any interface to 
# add the products by a user.

import os
import shutil
import django
import random
from faker import Faker
from datetime import datetime
from pathlib import Path

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "flushmart.settings")
django.setup()

from django.conf import settings
from customerproducts.infrastructure.models import (
    CustomerProductModel,
    CustomerProductWarrantyModel,
    CustomerProductCategoryModel,
)

fake = Faker()

TOILET_PRODUCTS = [
    {
        "title": "HydroFlush Supreme 2.0",
        "description": "A water-saving toilet with dual-flush technology, soft-close lid, and sleek design for modern homes."
    },
    {
        "title": "EcoClean WhisperJet",
        "description": "Built for silence and efficiency, this toilet features a whisper-quiet flush and anti-stain coating."
    },
    {
        "title": "TornadoBowl Classic",
        "description": "A traditional ceramic toilet with an ultra-powerful swirl flush and deep trapway for clog resistance."
    },
    {
        "title": "AquaZen Comfort Seat",
        "description": "Designed for long sittings, this model offers an ergonomic seat height and a gentle-closing lid."
    },
    {
        "title": "SmartFlush Touch Pro",
        "description": "A motion-sensor smart toilet with touchless flushing, deodorizer, and a night light for late-night visits."
    },
    {
        "title": "FlushMaster CompactFit",
        "description": "Ideal for small bathrooms, with a space-saving tank design and top-mount flush button."
    },
    {
        "title": "BidetBowl Fusion",
        "description": "Combines the benefits of a toilet and bidet, with adjustable spray settings and heated water."
    },
    {
        "title": "VelvetStream Deluxe",
        "description": "Luxury meets hygiene with a slow-closing seat, anti-bacterial glaze, and modern look."
    },
    {
        "title": "CrystalFlush Premier",
        "description": "Premium rimless design and cyclonic flush ensure a spotless bowl every time."
    },
    {
        "title": "FlushKing Royal Edition",
        "description": "A throne-worthy toilet with golden detailing and plush cushioning — unapologetically over-the-top."
    }
]

IMAGE_POOL = [
    "toilet1.jpg", "toilet2.jpg", "toilet3.jpg", "toilet4.jpg", "toilet5.webp", "placeholder.jpg"
]

# Path to images in static folder (source)
STATIC_IMAGE_DIR = Path(__file__).resolve().parent / "customerproducts" / "presentation" / "static" / "customer_products_images"

# Target media folder for ImageField (MEDIA_ROOT/customer_products_images/)
MEDIA_IMAGE_DIR = Path(settings.MEDIA_ROOT) / "customer_products_images"
MEDIA_IMAGE_DIR.mkdir(parents=True, exist_ok=True)


def copy_image_to_media(image_name):
    if not image_name:
        image_name = "placeholder.jpg"

    src = STATIC_IMAGE_DIR / image_name
    dst = MEDIA_IMAGE_DIR / image_name

    if not dst.exists():
        shutil.copyfile(src, dst)

    return f"customer_products_images/{image_name}"


def create_category():
    return CustomerProductCategoryModel.objects.create(name=fake.word().capitalize())


def create_warranty():
    return CustomerProductWarrantyModel.objects.create(
        warranty_start_date=datetime.now(), warranty_end_date=datetime.now()
    )


def run():
    categories = [create_category() for _ in range(3)]

    for _ in range(10):
        warranty = create_warranty()
        category = random.choice(categories)
        product = random.choice(TOILET_PRODUCTS)
        image_name = random.choice(IMAGE_POOL)
        image_path = copy_image_to_media(image_name)

        CustomerProductModel.objects.create(
            warranty=warranty,
            category=category,
            product_name=product["title"],
            description=product["description"],
            price=round(random.uniform(10, 5000), 2),
            image=image_path,  # ImageField expects relative path to MEDIA_ROOT
        )

    print("CustomerProducts populated.")


if __name__ == "__main__":
    run()
