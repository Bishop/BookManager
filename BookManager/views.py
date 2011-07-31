from django.http import HttpResponseRedirect
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from BookManager.models import Book, FileForm, File, EditionForm, Edition

class BookListView(ListView):
    paginate_by = 50
    template_name = 'book_list.html'
    context_object_name = 'books'

    def get_queryset(self):
        query = super(BookListView, self).get_queryset()
        if self.request.GET.has_key('keyword'):
            query = query.filter(title__icontains=self.request.GET['keyword'])
            self.paginate_by = query.count()
            self.kwargs.setdefault('page', 1)
        return query

    def get_context_data(self, **kwargs):
        context = super(BookListView, self).get_context_data(**kwargs)

        if self.request.GET.has_key('keyword'):
            context['search_value'] = self.request.GET['keyword']

        return context


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

    def get_context_data(self, **kwargs):
        context = super(BookDetailView, self).get_context_data(**kwargs)

        context.update({
            'file_form': FileForm(initial={'book': context['object']}),
            'edition_form': EditionForm(initial={'book': context['object']})
        })

        return context

    def get(self, request, **kwargs):
        return super(BookDetailView, self).get(request, **kwargs)

class BookAddInfoBaseView(CreateView):
    def get(self, request, *args, **kwargs):
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return Book.objects.get(pk=self.kwargs['pk']).get_absolute_url()

    def form_invalid(self, form):
        return HttpResponseRedirect(self.get_success_url())

class BookAddFileView(BookAddInfoBaseView):
    model = File

class BookAddEditionView(BookAddInfoBaseView):
    model = Edition

