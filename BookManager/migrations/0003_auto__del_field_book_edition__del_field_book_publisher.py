# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting field 'Book.edition'
        db.delete_column('BookManager_book', 'edition')

        # Deleting field 'Book.publisher'
        db.delete_column('BookManager_book', 'publisher')


    def backwards(self, orm):
        
        # Adding field 'Book.edition'
        db.add_column('BookManager_book', 'edition', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True), keep_default=False)

        # Adding field 'Book.publisher'
        db.add_column('BookManager_book', 'publisher', self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True), keep_default=False)


    models = {
        'BookManager.book': {
            'Meta': {'object_name': 'Book'},
            'author': ('django.db.models.fields.TextField', [], {}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pages': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.TextField', [], {}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'year': ('django.db.models.fields.DateField', [], {})
        }
    }

    complete_apps = ['BookManager']
