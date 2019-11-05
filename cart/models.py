from django.db import models
from django.utils import timezone

# Create your models here.
class Cart(models.Model):
    buyer_id = models.IntegerField(null=False)
    product_id = models.IntegerField(null=False)
    quantity = models.IntegerField(null=False,default=1)
    seller_id = models.IntegerField(null=False)
    date = models.DateTimeField(default=timezone.datetime.now())

    def __str__(self):
        return self.date