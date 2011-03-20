# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Products'
        db.create_table('selection_products', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('area', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['discovery.PaymentArea'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('price', self.gf('django.db.models.fields.FloatField')(max_length=500)),
        ))
        db.send_create_signal('selection', ['Products'])


    def backwards(self, orm):
        
        # Deleting model 'Products'
        db.delete_table('selection_products')


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
        },
        'selection.products': {
            'Meta': {'object_name': 'Products'},
            'area': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['discovery.PaymentArea']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'price': ('django.db.models.fields.FloatField', [], {'max_length': '500'})
        }
    }

    complete_apps = ['selection']
