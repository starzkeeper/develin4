# Generated by Django 4.1.2 on 2022-11-09 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('electronic', '0004_product_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(max_length=200, unique=True, verbose_name='URL'),
        ),
    ]
