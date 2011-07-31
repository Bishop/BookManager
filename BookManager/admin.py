from django.contrib import admin
from BookManager.models import Book, Publisher, Edition, File, Author

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'edition')

    def edition(self, obj):
        return ', '.join([e.isbn for e in obj.edition_set.all()])

class FileAdmin(admin.ModelAdmin):
    pass

class EditionAdmin(admin.ModelAdmin):
    pass

class PublisherAdmin(admin.ModelAdmin):
    pass

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'books_count')

    def name(self, obj):
        return str(obj)

admin.site.register(Book, BookAdmin)
admin.site.register(File, FileAdmin)
admin.site.register(Edition, EditionAdmin)
admin.site.register(Publisher, PublisherAdmin)
admin.site.register(Author, AuthorAdmin)