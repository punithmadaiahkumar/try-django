# Generated by Django 3.2.12 on 2022-04-01 10:31

from django.db import migrations, models
import recipes.validators


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0009_recipeingredientimage_extracted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipeingredient',
            name='quantity',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='recipeingredient',
            name='unit',
            field=models.CharField(blank=True, max_length=50, null=True, validators=[recipes.validators.validate_unit_of_measure]),
        ),
    ]