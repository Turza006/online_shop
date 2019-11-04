from django.db import models
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=10,null=False)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=50,null=False)
    id = models.IntegerField(null=False,primary_key=True)
    Date = models.DateTimeField(null=False,default=timezone.datetime.now())
    image = models.ImageField(null=True)
    price = models.IntegerField(null=False)
    seller = models.CharField(null=False,max_length=50)
    category = models.ManyToManyField(Category,null=False)




    def __str__(self):
        return "{id} {name}".format(id=self.id, name=self.name)