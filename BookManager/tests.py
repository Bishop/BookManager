"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.test.client import Client

class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)

class BookListTest(TestCase):
    def test_list(self):
        c = Client()
        response = c.get('/books/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'book_list.html')