from django.db import models
from django.utils import timezone

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=50,null=False)
    id = models.IntegerField(primary_key=True,null=False)
    email = models.CharField(max_length=50,null=False)
    Image = models.ImageField(upload_to='User/', null=True)
    address = models.CharField(max_length=100)
    date = models.DateTimeField(null=False,default=timezone.datetime.now())
    type = models.CharField(max_length=10,null=False)


    def __str__(self):
        return "{id} {name}".format(id=self.id, name=self.name)

