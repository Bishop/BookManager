from django.contrib import admin
from BookManager.models import Book, Publisher, Edition, File

class BookAdmin(admin.ModelAdmin):
    pass

class FileAdmin(admin.ModelAdmin):
    pass

class EditionAdmin(admin.ModelAdmin):
    pass

class PublisherAdmin(admin.ModelAdmin):
    pass

admin.site.register(Book, BookAdmin)
admin.site.register(File, FileAdmin)
admin.site.register(Edition, EditionAdmin)
admin.site.register(Publisher, PublisherAdmin)