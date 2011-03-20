from django.contrib.gis import admin
from django.contrib.gis.maps.google import GoogleMap
from models import PaymentArea


GMAP = GoogleMap(key='abcdefg') # Can also set GOOGLE_MAPS_API_KEY in settings

class GoogleAdmin(admin.OSMGeoAdmin):
    exclude = ('provider',)
    extra_js = [GMAP.api_url + GMAP.key]
    map_template = 'gis/admin/google.html'

admin.site.register(PaymentArea, GoogleAdmin)
