from django.contrib import admin
from .models import Book,Journal
# Register your models here.
admin.site.register(Book)
admin.site.register(Journal)