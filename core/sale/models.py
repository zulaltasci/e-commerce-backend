from django.db import models

# Create your models here.
class Sale(models.Model):
    id = models.AutoField(primary_key=True)
    product = models.IntegerField()
    quantity = models.IntegerField()
    total = models.DecimalField(max_digits=10, decimal_places=2)
    user = models.IntegerField()
    address = models.CharField(max_length=255)  
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

