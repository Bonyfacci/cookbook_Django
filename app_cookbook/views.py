from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.urls import reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from .models import Product, Recipe, RecipeProduct


def home(request: HttpRequest) -> HttpResponse:
    """
    Домашняя страница
    :param request: {method},
    :return: HttpResponse
    """
    return render(request, 'app_cookbook/home.html')


def add_product_to_recipe(request: HttpRequest, recipe_id: int, product_id: int, weight: int) -> HttpResponse:
    """
    Функция добавляет к указанному рецепту указанный продукт с указанным весом.
    Если в рецепте уже есть такой продукт, то функция должна поменять его вес в этом рецепте на указанный.
    :param request: {method},
    :param recipe_id: int,
    :param product_id: int,
    :param weight: int,
    :return: HttpResponse
    """
    try:
        if request.method == 'GET':
            product = Product.objects.get(id=product_id)
            recipe = Recipe.objects.get(id=recipe_id)

            recipe_product, _ = RecipeProduct.objects.get_or_create(recipe=recipe, product=product)
            recipe_product.weight = weight
            recipe_product.save()

            return HttpResponse('Продукт успешно добавлен к рецепту.')
    except Product.DoesNotExist as e:
        return HttpResponse(f'Продукт не найден! Ошибка: {e}')
    except Recipe.DoesNotExist as e:
        return HttpResponse(f'Рецепт не найден! Ошибка: {e}')


def cook_recipe(request: HttpRequest, recipe_id: int) -> HttpResponse:
    """
    Функция увеличивает на единицу количество приготовленных блюд для каждого продукта, входящего в указанный рецепт.
    :param request: {method},
    :param recipe_id: int,
    :return: HttpResponse
    """
    try:
        if request.method == 'GET':
            recipe = Recipe.objects.get(id=recipe_id)
            recipe_products = recipe.recipeproduct_set.all()

            for recipe_product in recipe_products:
                product = recipe_product.product
                product.times_cooked += 1
                product.save()

            return HttpResponse('Рецепт успешно приготовлен.')
    except Recipe.DoesNotExist as e:
        return HttpResponse(f'Рецепт не найден! Ошибка: {e}')


def show_recipes_without_product(request: HttpRequest, product_id: int) -> HttpResponse:
    """
    Функция возвращает HTML страницу, на которой размещена таблица.
    В таблице отображены id и названия всех рецептов,
    в которых указанный продукт отсутствует, или присутствует в количестве меньше 10 грамм.
    :param request: {method},
    :param product_id: int,
    :return: HttpResponse
    """
    try:
        if request.method == 'GET':
            product = Product.objects.get(id=product_id)

            recipe_product_list = Recipe.objects.filter(
                recipeproduct__product=product,
                recipeproduct__weight__gte=10
            )

            return render(
                request, 'app_cookbook/recipe_product_list.html',
                {'object_list': recipe_product_list, 'product_name': product.name}
            )
    except Product.DoesNotExist as e:
        return HttpResponse(f'Продукт не найден! Ошибка: {e}')


class ProductCreateView(CreateView):
    model = Product
    template_name = 'app_cookbook/product_form.html'
    fields = ('name',)

    def get_success_url(self):
        return reverse('app_cookbook:products')


class ProductListView(ListView):
    model = Product


class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'app_cookbook/product_form.html'
    fields = ('name',)

    def get_success_url(self):
        return reverse('app_cookbook:products')


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'app_cookbook/product_delete_confirm.html'

    def get_success_url(self):
        return reverse('app_cookbook:products')


class RecipeCreateView(CreateView):
    model = Recipe
    template_name = 'app_cookbook/recipe_form.html'
    fields = ('name', 'products')

    def get_success_url(self):
        return reverse('app_cookbook:recipes')


class RecipeListView(ListView):
    model = Recipe


class RecipeUpdateView(UpdateView):
    model = Recipe
    template_name = 'app_cookbook/recipe_form.html'
    fields = ('name', 'products',)

    def get_success_url(self):
        return reverse('app_cookbook:recipes')


class RecipeDeleteView(DeleteView):
    model = Recipe
    template_name = 'app_cookbook/recipe_delete_confirm.html'

    def get_success_url(self):
        return reverse('app_cookbook:recipes')
