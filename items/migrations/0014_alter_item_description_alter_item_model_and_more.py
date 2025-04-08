# Generated by Django 5.1.7 on 2025-03-27 03:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("items", "0013_remove_item_user_cart_cartitem"),
    ]

    operations = [
        migrations.AlterField(
            model_name="item",
            name="description",
            field=models.TextField(
                blank=True, null=True, verbose_name="Описание товара"
            ),
        ),
        migrations.AlterField(
            model_name="item",
            name="model",
            field=models.CharField(
                blank=True, max_length=255, null=True, verbose_name="Модель"
            ),
        ),
        migrations.AlterField(
            model_name="item",
            name="production",
            field=models.CharField(
                blank=True, max_length=255, null=True, verbose_name="Производство"
            ),
        ),
    ]
