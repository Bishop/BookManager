from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from BookManager.models import Book

class BookListView(ListView):
    paginate_by = 10
    template_name = 'book_list.html'
    context_object_name = 'books'

class BookCreateView(CreateView):
    model = Book
    template_name = 'book_form.html'

class BookUpdateView(UpdateView):
    model = Book
    template_name = 'book_form.html'

class BookDetail(DetailView):
    model = Book
    template_name = 'book_detail.html'
    context_object_name = 'book'