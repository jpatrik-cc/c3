# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting model 'Products'
        db.delete_table('selection_products')

        # Adding model 'ProductArea'
        db.create_table('selection_productarea', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('area', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['discovery.PaymentArea'])),
            ('product', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['selection.Product'])),
            ('amount', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('available', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal('selection', ['ProductArea'])

        # Adding model 'Product'
        db.create_table('selection_product', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('price', self.gf('django.db.models.fields.FloatField')(max_length=500)),
        ))
        db.send_create_signal('selection', ['Product'])


    def backwards(self, orm):
        
        # Adding model 'Products'
        db.create_table('selection_products', (
            ('price', self.gf('django.db.models.fields.FloatField')(max_length=500)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('area', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['discovery.PaymentArea'])),
        ))
        db.send_create_signal('selection', ['Products'])

        # Deleting model 'ProductArea'
        db.delete_table('selection_productarea')

        # Deleting model 'Product'
        db.delete_table('selection_product')


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
        'selection.product': {
            'Meta': {'object_name': 'Product'},
            'area': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['discovery.PaymentArea']", 'through': "orm['selection.ProductArea']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'price': ('django.db.models.fields.FloatField', [], {'max_length': '500'})
        },
        'selection.productarea': {
            'Meta': {'object_name': 'ProductArea'},
            'amount': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'area': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['discovery.PaymentArea']"}),
            'available': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['selection.Product']"})
        }
    }

    complete_apps = ['selection']
