#from django.db import models

# Create your models here.

from django.contrib.gis.db import models

class WorldBorders(models.Model):
    # Regular Django fields corresponding to the attributes in the
    # world borders shapefile.
    name = models.CharField(max_length=50)
    area = models.IntegerField()
    pop2005 = models.IntegerField('Population 2005')
    fips = models.CharField('FIPS Code', max_length=2)
    iso2 = models.CharField('2 Digit ISO', max_length=2)
    iso3 = models.CharField('3 Digit ISO', max_length=3)
    un = models.IntegerField('United Nations Code')
    region = models.IntegerField('Region Code')
    subregion = models.IntegerField('Sub-Region Code')
    lon = models.FloatField()
    lat = models.FloatField()

    # GeoDjango-specific: a geometry field (MultiPolygonField), and
    # overriding the default manager with a GeoManager instance.
    mpoly = models.MultiPolygonField()
    objects = models.GeoManager()

    # So the model is pluralized correctly in the admin.
    class Meta:
        verbose_name_plural = "World Borders"

    # Returns the string representation of the model.
    def __unicode__(self):
        return self.name

# This is an auto-generated Django model module created by ogrinspect.
#from django.contrib.gis.db import models

#class WorldBorders(models.Model):
    #fips = models.CharField(max_length=2)
    #iso2 = models.CharField(max_length=2)
    #iso3 = models.CharField(max_length=3)
    #un = models.IntegerField()
    #name = models.CharField(max_length=50)
    #area = models.IntegerField()
    #pop2005 = models.IntegerField()
    #region = models.IntegerField()
    #subregion = models.IntegerField()
    #lon = models.FloatField()
    #lat = models.FloatField()
    #geom = models.MultiPolygonField(srid=4326)
    #objects = models.GeoManager()

# Auto-generated `LayerMapping` dictionary for WorldBorders model
worldborders_mapping = {
    'fips' : 'FIPS',
    'iso2' : 'ISO2',
    'iso3' : 'ISO3',
    'un' : 'UN',
    'name' : 'NAME',
    'area' : 'AREA',
    'pop2005' : 'POP2005',
    'region' : 'REGION',
    'subregion' : 'SUBREGION',
    'lon' : 'LON',
    'lat' : 'LAT',
    'geom' : 'MULTIPOLYGON',
}
