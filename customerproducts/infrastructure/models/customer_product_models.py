from django.db import models

# The general product which the user will interact with.
class CustomerProductModel(models.Model):
    warranty = models.OneToOneField(
        "CustomerProductWarrantyModel",
        on_delete=models.CASCADE,
        related_name="customer_product_warranty",
    )
    category = models.ForeignKey(
        "CustomerProductCategoryModel",
        on_delete=models.CASCADE,
        related_name="customer_product_category",
    )

    product_name = models.CharField(default="")
    description = models.TextField(default="")
    price = models.DecimalField(default=0.0, decimal_places=2, max_digits=10)


# General feature section so that we can have many extra features for each product.
class CustomerFeatureSectionModel(models.Model):
    customer_product = models.ForeignKey(
        "CustomerProductModel", on_delete=models.CASCADE, related_name="customer_product"
    )
    section_title = models.CharField(default="")


# There can be different names and description for each feature in the feature section,
# need to know which feature relates to which feature section.
class CustomerProductFeatureModel(models.Model):
    customer_product_feature_section = models.ForeignKey(
        "CustomerFeatureSectionModel",
        on_delete=models.CASCADE,
        related_name="customer_product_feature_section",
    )
    name = models.CharField(default="")
    description = models.CharField(default="")


class CustomerProductWarrantyModel(models.Model):
    warranty_start_date = models.DateField()
    warranty_end_date = models.DateField()


class CustomerProductCategoryModel(models.Model):
    name = models.CharField(default="")
