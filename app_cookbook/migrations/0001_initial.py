# Generated by Django 5.0.1 on 2024-01-26 21:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Product name', max_length=150, verbose_name='Название продукта')),
                ('times_cooked', models.IntegerField(default=0, help_text='Product used ... times', verbose_name='Продукт использовался ... раз')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Recipe name', max_length=150, verbose_name='Название рецепта')),
            ],
            options={
                'verbose_name': 'Рецепт',
                'verbose_name_plural': 'Рецепты',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='RecipeProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.IntegerField(default=0, help_text='Weight of product, g', verbose_name='Вес продукта, г')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_cookbook.product', verbose_name='Продукт')),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_cookbook.recipe', verbose_name='Рецепт')),
            ],
            options={
                'verbose_name': 'Рецепт-Продукт',
                'verbose_name_plural': 'Рецепты-Продукты',
                'unique_together': {('recipe', 'product')},
            },
        ),
        migrations.AddField(
            model_name='recipe',
            name='products',
            field=models.ManyToManyField(through='app_cookbook.RecipeProduct', to='app_cookbook.product', verbose_name='Продукты'),
        ),
    ]
