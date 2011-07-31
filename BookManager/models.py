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
        return u"{0} ({1}) [{2}]".format(self.title, self.author, self.year)

class File(ProtocolModel):
    book = models.ForeignKey(Book)
    path = models.CharField(max_length=200)
    note = models.TextField(**nullable)

    def __unicode__(self):
        return self.path

class Publisher(ProtocolModel):
    title = models.CharField(max_length=100, unique=True)
    url = models.URLField(unique=True, verify_exists=False, **nullable)
    book = models.ManyToManyField(Book, through='Edition')

    def __unicode__(self):
        return self.title

class Edition(ProtocolModel):
    isbn = models.CharField(max_length=20)
    book = models.ForeignKey(Book)
    publisher = models.ForeignKey(Publisher, **nullable)

    def __unicode__(self):
        return self.isbn

class BookForm(ModelForm):
    class Meta:
        model = Book

class FileForm(ModelForm):
    class Meta:
        model = File
        widgets = {
            'book': HiddenInput(),
        }