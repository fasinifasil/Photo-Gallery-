from django.contrib import admin

from PhotoApp.models import Category, Photo

# Register your models here.
admin.site.register(Category)
admin.site.register(Photo)