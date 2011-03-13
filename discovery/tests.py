import json

from django.test import TestCase
from django.test.client import Client
from django.core.urlresolvers import reverse
from django.contrib.gis.geos import Point, Polygon

from cococloud.discovery.models import PaymentArea
from cococloud.customer.models import Customer

class PaymentAreasTest(TestCase):
    def setUp(self):
        self.centralstation = Polygon([ 
                [ 13.136215, 55.702742 ], [ 13.163681, 55.737162 ], 
                [ 13.224792, 55.736389 ], [ 13.259125, 55.698099 ], 
                [ 13.209000, 55.682424 ], [ 13.175354, 55.683391 ], 
                [ 13.136215, 55.702742 ] ])
        self.customer = Customer.objects.create(name='SJ')
        self.area = PaymentArea.objects.create(identifier='SJ Lund',
                                               area=self.centralstation,
                                               owner=self.customer)
        self.client = Client()

    def test_areas_by_point(self):
        """
        Tests that the areas are retuned when querying for a location
        """
        p = Point(13.18686, 55.70605)
        self.failUnless(self.centralstation.contains(p))
        self.failUnless(PaymentArea.objects.all()[0].area.contains(p))
        self.failUnless(self.area in list(PaymentArea.objects.filter(area__contains=p)))

    def test_local_options_view(self):
        """
        Get the local options based on the position
        """
        response = self.client.get(
            reverse('local_discovery')+'?position=13.18686,55.70605')
        self.failUnlessEqual(response.status_code, 200)
        self.failUnlessEqual(json.loads(response.content), 
                             [{u'owner': u'SJ', u'identifier': u'SJ Lund'}])

        response = self.client.get(
            reverse('local_discovery')+'?position=34.18686,25.70605')
        self.failUnlessEqual(response.status_code, 200)
        self.failUnlessEqual(json.loads(response.content), [])
