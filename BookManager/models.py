from __future__ import unicode_literals

import os
from django.core.urlresolvers import reverse
from django.db import models
from django.db.models import permalink
from django.forms.models import ModelForm
from django.forms import HiddenInput

nullable = {'null': True, 'blank': True}

class ProtocolModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Book(ProtocolModel):
    title = models.TextField()
    author = models.TextField()
    year = models.DateField()
    pages = models.IntegerField(**nullable)

    @permalink
    def get_absolute_url(self):
        return 'book_detail', [self.pk]

    def __unicode__(self):
        return "{0} ({1}) [{2}]".format(self.title, self.author, self.year)

    def un_file_name(self):
        r = "{0} - {1} ({2})".format(self.author, self.title, self.year.year, )
        if self.edition_set.count():
            r += ''.join([" [ISBN {0} - {1}]".format(e.isbn, e.publisher) for e in self.edition_set.all()])
        return r
    
class File(ProtocolModel):
    book = models.ForeignKey(Book)
    path = models.CharField(max_length=200)
    note = models.TextField(**nullable)

    def __unicode__(self):
        return self.path

    def file_name(self):
        return os.path.split(self.path)[1]

class Publisher(ProtocolModel):
    title = models.CharField(max_length=100, unique=True)
    url = models.URLField(unique=True, verify_exists=False, **nullable)
    book = models.ManyToManyField(Book, through='Edition')

    def __unicode__(self):
        return self.title

class Edition(ProtocolModel):
    isbn = models.CharField(max_length=20, verbose_name='ISBN', unique=True)
    book = models.ForeignKey(Book)
    publisher = models.ForeignKey(Publisher, **nullable)

    def __unicode__(self):
        return self.isbn

class Author(ProtocolModel):
    display_name = models.CharField(max_length=200)
    canonical_name = models.CharField(max_length=200, **nullable)
    original_name = models.CharField(max_length=200, **nullable)
    book = models.ManyToManyField(Book, related_name='trusted_author')

    def books_count(self):
        return self.book.count()

    def __unicode__(self):
        r = self.display_name
        if self.canonical_name is not None:
            r += ' ({0})'.format(self.canonical_name)
        return r

class BookForm(ModelForm):
    class Meta:
        model = Book

class FileForm(ModelForm):
    class Meta:
        model = File
        widgets = {
            'book': HiddenInput(),
        }

class EditionForm(ModelForm):
    class Meta:
        model = Edition
        widgets = {
            'book': HiddenInput(),
        }