from django.test import TestCase
from django.contrib.gis.geos import Point, Polygon

from cococloud.discovery.models import PaymentArea
from cococloud.customer.models import Customer

class PaymentAreasTest(TestCase):
    def test_areas_by_point(self):
        """
        Tests that the areas are retuned when querying for a location
        """
        p = Point(13.18686, 55.70605)
        centralstation = Polygon([ [ 13.136215, 55.702742 ], [ 13.163681, 55.737162 ], 
                                   [ 13.224792, 55.736389 ], [ 13.259125, 55.698099 ], 
                                   [ 13.209000, 55.682424 ], [ 13.175354, 55.683391 ], 
                                   [ 13.136215, 55.702742 ] ])
        self.failUnless(centralstation.contains(p))
        customer = Customer.objects.create(name='SJ')
        area = PaymentArea.objects.create(identifier='SJ Lund',
                                          area=centralstation,
                                          owner=customer)
        self.failUnless(area in list(PaymentArea.objects.filter(area__contains=p)))
