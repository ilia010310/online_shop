# Generated by Django 5.0 on 2023-12-25 12:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0016_itemimages_delete_itemimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemimages',
            name='item',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.item'),
        ),
    ]
