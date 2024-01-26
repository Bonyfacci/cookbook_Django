from django.db import models


class Product(models.Model):
    """
    Модель Продукта
    """
    name = models.CharField(
        max_length=150,
        verbose_name='Название продукта',
        help_text='Product name'
    )
    times_cooked = models.IntegerField(
        default=0,
        verbose_name='Продукт использовался ... раз',
        help_text='Product used ... times'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ('name',)


class Recipe(models.Model):
    """
    Модель Рецепта
    """
    name = models.CharField(
        max_length=150,
        verbose_name='Название рецепта',
        help_text='Recipe name'
    )
    products = models.ManyToManyField(
        Product,
        through='RecipeProduct',
        verbose_name='Продукты'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'
        ordering = ('name',)


class RecipeProduct(models.Model):
    """
    Модель Рецепт с продуктом
    """
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        verbose_name='Рецепт'
    )

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        verbose_name='Продукт'
    )

    weight = models.IntegerField(
        default=0,
        verbose_name='Вес продукта, г',
        help_text='Weight of product, g'
    )

    def __str__(self):
        return f'{self.recipe.name} - {self.product.name}{self.weight}г.'

    class Meta:
        verbose_name = 'Рецепт-Продукт'
        verbose_name_plural = 'Рецепты-Продукты'
        unique_together = ('recipe', 'product')
