from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    file = models.FileField(upload_to='products/')  # for digital content
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='products/',default='products/1.png')  # for product image

    def __str__(self):
        return self.title



