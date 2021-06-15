# Register your models here.
from django.contrib import admin
from .models import Category, Product
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    List_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    List_display = ['name', 'slug', 'price','available', 'created', 'updated']
    List_filter = ['available', 'created', 'updated']
    List_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('name',)}