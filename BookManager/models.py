from django.db import models

nullable = {'null': True, 'blank': True}

class Book(models.Model):
    title = models.TextField()
    author = models.TextField()
    year = models.DateField()
    edition = models.CharField(max_length=50, **nullable)
    publisher = models.CharField(max_length=150, **nullable)
    pages = models.IntegerField(**nullable)
    