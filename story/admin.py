from django.contrib import admin

from .models import Author, Category, Post, Recipe, FeaturedPost, Advertise

admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Recipe)
admin.site.register(FeaturedPost)
admin.site.register(Advertise)