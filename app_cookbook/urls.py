from django.urls import path

from app_cookbook.apps import AppCookbookConfig
from app_cookbook.views import home, add_product_to_recipe, cook_recipe, show_recipes_without_product, ProductListView, \
    ProductCreateView, ProductUpdateView, ProductDeleteView, RecipeListView, RecipeCreateView, RecipeUpdateView, \
    RecipeDeleteView

app_name = AppCookbookConfig.name

urlpatterns = [
    path('', home, name='home'),  # http://127.0.0.1:8000/

    path('add_product_to_recipe/<int:recipe_id>/<int:product_id>/<int:weight>/', add_product_to_recipe, name='add-product'),
    path('cook_recipe/<int:recipe_id>/', cook_recipe, name='prepare_the_recipe'),
    path('recipe_product_list/<int:product_id>/', show_recipes_without_product, name='recipe_product_list'),

    # Продукт
    path('products/', ProductListView.as_view(), name='products'),
    path('product/add/', ProductCreateView.as_view(), name='product_create'),
    path('product/edit/<int:pk>/', ProductUpdateView.as_view(), name='product_edit'),
    path('product/delete/<int:pk>/', ProductDeleteView.as_view(), name='product_delete'),

    # Рецепт
    path('recipes/', RecipeListView.as_view(), name='recipes'),
    path('recipe/add/', RecipeCreateView.as_view(), name='recipe_create'),
    path('recipe/edit/<int:pk>/', RecipeUpdateView.as_view(), name='recipe_edit'),
    path('recipe/delete/<int:pk>/', RecipeDeleteView.as_view(), name='recipe_delete'),
]
