from django.contrib import admin
from .models import Book, Author

admin.site.register(Book)
admin.site.register(Author)

class BookAdmin(admin.ModelAdmin):
    model = Book
    list_display = ('id',)

# Register your models here.
