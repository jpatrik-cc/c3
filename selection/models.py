from django.contrib.gis.db import models
from cococloud.discovery.models import PaymentArea


# Create your models here.
# Provider/products (web provider, local, auto) 
# Customize (via custom forms)
# Provider classes. Selection config model.

"""
Generalized cases:
 * Parking (Ghent):
   - Only one product
   - Open/Close hours
   - Product options affect pricing
   - Limited quantity per area
   - Custom parking provider

 * Services (Max):
   - Open/Close hours
   - Unlimited but can be flagged as not available
   - Local provider
   
 * Retail (Ikea):
   - Open/Close hours
   - Limited quantity 
   - Likely use a web provider or custom provider

 * Local Traffic:
   - Time sensitive
   - Likely use a web provider or custom provider

"""

class Product(models.Model):
    area = models.ManyToManyField(PaymentArea, through='ProductArea')
    name = models.CharField(max_length=500)
    price = models.FloatField(max_length=500)

    def __unicode__(self):
        return self.name

class ProductArea(models.Model):
    area = models.ForeignKey(PaymentArea)
    product = models.ForeignKey(Product)
    amount = models.IntegerField(blank=True, null=True)
    available = models.BooleanField(default=True)
    
