from django.contrib import admin
from BookManager.models import Book, Publisher, Edition, File, Author

class BookAdmin(admin.ModelAdmin):
    pass

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