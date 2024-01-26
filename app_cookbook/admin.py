from django.contrib import admin

from app_cookbook.models import Product, Recipe, RecipeProduct


@admin.register(Product)
class ProductListAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'times_cooked',)
    search_fields = ('name',)


@admin.register(Recipe)
class RecipeListAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name',)
    search_fields = ('name',)


@admin.register(RecipeProduct)
class RecipeProductListAdmin(admin.ModelAdmin):
    list_display = ('pk', 'recipe', 'product', 'weight',)
