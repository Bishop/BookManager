from django.core.urlresolvers import reverse
from django.db import models
from django.forms.models import ModelForm

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

    def get_absolute_url(self):
        return reverse('book_detail', args=[self.pk])

class File(ProtocolModel):
    book = models.ForeignKey(Book)
    path = models.URLField()
    note = models.TextField(**nullable)

class Publisher(ProtocolModel):
    title = models.CharField(max_length=100, unique=True)
    url = models.URLField(unique=True, **nullable)

class Edition(ProtocolModel):
    isbn = models.CharField(max_length=20)
    book = models.ForeignKey(Book)
    publisher = models.ForeignKey(Publisher, **nullable)

class BookForm(ModelForm):
    class Meta:
        model = Book