from django.http import HttpResponseRedirect
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from BookManager.models import Book, FileForm, File

class BookListView(ListView):
    paginate_by = 50
    template_name = 'book_list.html'
    context_object_name = 'books'

class BookCreateView(CreateView):
    model = Book
    template_name = 'book_form.html'

class BookUpdateView(UpdateView):
    model = Book
    template_name = 'book_form.html'

class BookDetailView(DetailView):
    model = Book
    template_name = 'book_detail.html'
    context_object_name = 'book'

    def render_to_response(self, context, **response_kwargs):
        context['file_form'] = FileForm(initial={'book': context['object']})
        return super(BookDetailView, self).render_to_response(context, **response_kwargs)

    def get(self, request, **kwargs):
        return super(BookDetailView, self).get(request, **kwargs)


class BookAddFileView(CreateView):
    model = File

    def get(self, request, *args, **kwargs):
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return Book.objects.get(pk=self.kwargs['pk']).get_absolute_url()

    def form_invalid(self, form):
        return HttpResponseRedirect(self.get_success_url())






    