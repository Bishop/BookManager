# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Book'
        db.create_table('BookManager_book', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.TextField')()),
            ('author', self.gf('django.db.models.fields.TextField')()),
            ('year', self.gf('django.db.models.fields.DateField')()),
            ('edition', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('publisher', self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True)),
            ('pages', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal('BookManager', ['Book'])


    def backwards(self, orm):
        
        # Deleting model 'Book'
        db.delete_table('BookManager_book')


    models = {
        'BookManager.book': {
            'Meta': {'object_name': 'Book'},
            'author': ('django.db.models.fields.TextField', [], {}),
            'edition': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pages': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'publisher': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.TextField', [], {}),
            'year': ('django.db.models.fields.DateField', [], {})
        }
    }

    complete_apps = ['BookManager']
