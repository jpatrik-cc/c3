# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'PaymentArea'
        db.create_table('discovery_paymentarea', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('identifier', self.gf('django.db.models.fields.CharField')(max_length=500, null=True, blank=True)),
            ('area', self.gf('django.contrib.gis.db.models.fields.PolygonField')()),
            ('owner', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['customer.Customer'])),
            ('provider', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal('discovery', ['PaymentArea'])


    def backwards(self, orm):
        
        # Deleting model 'PaymentArea'
        db.delete_table('discovery_paymentarea')


    models = {
        'customer.customer': {
            'Meta': {'object_name': 'Customer'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'discovery.paymentarea': {
            'Meta': {'object_name': 'PaymentArea'},
            'area': ('django.contrib.gis.db.models.fields.PolygonField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'identifier': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['customer.Customer']"}),
            'provider': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['discovery']
