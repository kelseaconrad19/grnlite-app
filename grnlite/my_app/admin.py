from django.contrib import admin
from .models import Reader, Book

admin.site.register(Reader)
admin.site.register(Book)