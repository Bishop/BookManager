from django.views.generic.list import ListView

class BookListView(ListView):
    paginate_by = 10
    template_name = 'book_list.html'
    context_object_name = 'book'
