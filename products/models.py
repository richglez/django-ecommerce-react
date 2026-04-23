from django.db import models
from django.utils import timezone


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=500, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    # image = models.ImageField(upload_to='product_images/')

    # Metadatos útiles
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)  # Soft delete

    def soft_delete(self):
        self.deleted_at = timezone.now()
        self.save()

    def restore(self):
        self.deleted_at = None
        self.save()

    def __str__(self):
        return self.name
