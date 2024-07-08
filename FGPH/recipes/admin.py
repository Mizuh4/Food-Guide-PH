from django.contrib import admin

from .models import Author, Recipe

# Register your models here.
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("recipes",)
    
class RecipeAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "description")

admin.site.register(Author)
admin.site.register(Recipe)