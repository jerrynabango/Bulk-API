from django.db import models


# Create your models here.
# Product Model.
class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='products_images/', blank=True,
                              null=True)

    def __str__(self):
        return self.name

    def get_image(self):
        if self.image_file:
            return self.image_file.url
        return None


# ProductVariant Model.
class ProductVariant(models.Model):
    id = models.AutoField(primary_key=True)
    # sku - Stock Keeping Unit.
    sku = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    details = models.TextField()
    product = models.ForeignKey(Product, related_name='variants',
                                on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} ({self.sku})"
