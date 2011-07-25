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
    edition = models.CharField(max_length=50, **nullable)
    publisher = models.CharField(max_length=150, **nullable)
    pages = models.IntegerField(**nullable)


class BookForm(ModelForm):
    class Meta:
        model = Book