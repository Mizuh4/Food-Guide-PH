from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Author, Recipe, User

# Register your models here.
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("recipes",)
    
class RecipeAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "description")

admin.site.register(User, UserAdmin)
admin.site.register(Author)
admin.site.register(Recipe)