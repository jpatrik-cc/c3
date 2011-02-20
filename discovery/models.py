from django.contrib.gis.db import models

from cococloud.customer.models import Customer

class PaymentArea(models.Model):
    identifier = models.CharField(max_length=500, blank=True, null=True)
    area = models.PolygonField()
    owner = models.ForeignKey(Customer)

    def __unicode__(self):
        return self.identifier and self.identifier or ("%s's area" % self.owner)
