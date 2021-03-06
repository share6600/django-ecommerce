import os
import random
from django.db import models

def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    print(instance)
    print(filename)
    new_filename = random.randint(1, 9999999999)
    name, ext = get_filename_ext(filename)
    final_filename = f'{new_filename}{ext}'
    return f'products/{new_filename}/{final_filename}'
class ProductQuerySet(models.query.QuerySet):
    def featured(self):
        return self.filter(featured=True)
class ProductManager(models.Manager):
    def features(self):
        return ProductQuerySet(self.model,using=self.db)

    def get_by_id(self,id):
         qs= self.get_queryset().filter(id=id)
         if qs.count()==1:
           return qs.first()
         return None

class Product(models.Model):
    title       = models.CharField(max_length=120)
    description = models.TextField()
    price       = models.DecimalField( max_digits=5, decimal_places=2)
    image       = models.ImageField(upload_to=upload_image_path, max_length=100,null=True,blank=True)
    featured    = models.BooleanField(default=False)
    objects=ProductManager()
    def __str__(self):
        return self.title