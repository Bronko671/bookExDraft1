from django.contrib import admin

from .models import MainMenu, Book, Review

# Register your models here.

admin.site.register(MainMenu)
admin.site.register(Book)
admin.site.register(Review)

