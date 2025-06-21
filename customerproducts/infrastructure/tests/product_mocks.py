from django.core.files.uploadedfile import SimpleUploadedFile
from django.conf import settings
import tempfile
from faker import Faker
import faker_commerce
from model_bakery.recipe import Recipe
    
def _mock_image():
    _temp_media = tempfile.mkdtemp()
    settings.MEDIA_ROOT = _temp_media 
    return SimpleUploadedFile(name='test_image.jpg', content=b'\x47\x49')

def mock_product():
    faker = Faker()
    faker.add_provider(faker_commerce.Provider)
    return Recipe(
    "CustomerProductModel",
    product_name=lambda: faker.ecommerce_name(),
    description=lambda: faker.text(max_nb_chars=10000),
    price=lambda: faker.pydecimal(left_digits=7, right_digits=2, 
                                  positive=True),
    image=_mock_image()
    )  
