# Generated by Django 5.1.6 on 2025-05-14 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebProjecte', '0004_remove_card_image_url_remove_cardset_image_url_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='image',
            field=models.ImageField(upload_to='card_images'),
        ),
        migrations.AlterField(
            model_name='cardset',
            name='image',
            field=models.ImageField(upload_to='card_sets'),
        ),
    ]
