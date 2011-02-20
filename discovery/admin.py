from django.contrib.gis import admin
from models import PaymentArea

admin.site.register(PaymentArea, admin.GeoModelAdmin)
