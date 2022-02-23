from distutils.command.upload import upload
from email.mime import image
from turtle import title
from django.db import models

# Create your models here.
class Product(models.Model):
    pid = models.IntegerField(primary_key=True, auto_created=True)
    title = models.CharField(max_length=20)
    description = models.TextField(max_length=300)
    price = models.FloatField()
    stock = models.BooleanField(default=True, null=False)
    image=models.ImageField(upload_to="productimage/")
    catagory = models.TextField(max_length=20, null=True, blank=True)
    delivery = models.SmallIntegerField(default=3, null=False)

    def __str__(self):
        return self.title
