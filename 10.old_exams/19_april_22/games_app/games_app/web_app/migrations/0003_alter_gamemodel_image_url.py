# Generated by Django 4.1.2 on 2022-10-21 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_app', '0002_create_model_game_model_and_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gamemodel',
            name='image_url',
            field=models.URLField(),
        ),
    ]
