# Generated by Django 3.2.12 on 2022-03-30 11:10

from django.db import migrations, models
import recipes.models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0007_alter_recipeingredientimage_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipeingredientimage',
            name='image',
            field=models.ImageField(upload_to=recipes.models.recipe_ingredient_image_upload_handler),
        ),
    ]
