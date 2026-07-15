from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100, blank=False,null=False)
    description = models.TextField()
    price = models.PositiveIntegerField(blank=False, default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name 