# Generated by Django 3.2.12 on 2022-03-16 11:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipeingredient',
            old_name='quanity',
            new_name='quantity',
        ),
    ]
