# Generated by Django 4.0.4 on 2022-06-08 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0002_items_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='image',
            field=models.ImageField(blank=True, upload_to='items-images'),
        ),
        migrations.AlterField(
            model_name='items',
            name='items',
            field=models.ManyToManyField(blank=True, to='market.item'),
        ),
    ]
