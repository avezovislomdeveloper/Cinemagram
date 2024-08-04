from django.contrib import admin
from . models import Movies, Category, Comment

# Register your models here.

admin.site.register(Movies)
admin.site.register(Category)
admin.site.register(Comment)