from django.db import models
from django.core.exceptions import ValidationError
import re
def nameFiledValidator(value):
    x = re.findall("\d", value)
    if len(value)== len(x):
        raise ValidationError("This field accepts char only only")
    else:
        return value
        
class Brands(models.Model):
    Id = models.AutoField(primary_key = True)
    BrandName = models.CharField(max_length = 200)
    def __str__(self):
        return str(self.BrandName)

        
class products(models.Model):
    Id = models.AutoField(primary_key = True)
    productName = models.CharField(max_length= 200, validators=[nameFiledValidator])
    description=models.TextField(blank=True)
    price=models.FloatField()
    brand=models.ForeignKey(Brands, on_delete = models.CASCADE, related_name='tracks')
    
    def __str__(self):
        return str(self.productName)
        
class shops(models.Model):
    Id = models.AutoField(primary_key = True)
    Name = models.CharField(max_length= 200, validators=[nameFiledValidator])
    product=models.ManyToManyField(products, related_name='prdcts')
    def __str__(self):
        return str(self.Name)
