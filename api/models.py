from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100,)
    description = models.TextField()
    price = models.DecimalField(blank=False, null=False, decimal_places=2, max_digits=10)
    stock=models.DecimalField(blank=False, null=False, decimal_places=2, max_digits=10)
    created_at = models.DateTimeField(auto_now_add=True)
    created_date=models.DateField()

    def __str__(self):
        return f'{self.name}'    