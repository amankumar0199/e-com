from django.db import models

# Create your models here.
class Order(models.Model):
    product_name = models.CharField(max_length=100)
    customer_name = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} - {self.product_name} by {self.customer_name}"