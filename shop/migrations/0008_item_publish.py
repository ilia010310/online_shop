# Generated by Django 5.0 on 2023-12-20 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_alter_item_description_alter_item_length_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='publish',
            field=models.DateTimeField(default='2023-12-15 00:00'),
        ),
    ]
