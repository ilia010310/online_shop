# Generated by Django 5.0 on 2023-12-25 12:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0017_alter_itemimages_item'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemimages',
            name='item',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='item', to='shop.item'),
        ),
    ]
