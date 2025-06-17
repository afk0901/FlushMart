from django.db import models

"""
Products for a customer to interact with.
"""


# The general product which the user will interact with.
class CustomerProduct(models.Model):
    warranty = models.OneToOneField(
        "CustomerProductWarranty",
        on_delete=models.CASCADE,
        related_name="customer_product_warranty",
    )
    category = models.ForeignKey(
        "CustomerProductCategory",
        on_delete=models.CASCADE,
        related_name="customer_product_category",
    )
    product_name = models.CharField(default="")
    description = models.TextField(default="")
    price = models.DecimalField(default=0.0, decimal_places=2, max_digits=10)
    image = models.ImageField(upload_to="./media/customer_products_images/")


# General feature section so that we can have many extra features for each product.
class CustomerProductFeatureSection(models.Model):
    customer_product = models.ForeignKey(
        "CustomerProduct", on_delete=models.CASCADE, related_name="customer_product"
    )
    section_title = models.CharField(default="")


# There can be different names and description for each feature in the feature section,
# need to know which feature relates to which feature section.
class CustomerProductFeature(models.Model):
    customer_product_feature_section = models.ForeignKey(
        "CustomerProduct",
        on_delete=models.CASCADE,
        related_name="customer_product_feature_section",
    )
    name = models.CharField(default="")
    description = models.CharField(default="")


class CustomerProductWarranty(models.Model):
    warranty_start_date = models.DateField()
    warranty_end_date = models.DateField()


class CustomerProductCategory(models.Model):
    name = models.CharField(default="")
