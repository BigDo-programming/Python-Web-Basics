# Generated by Django 4.1.2 on 2022-10-10 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0004_alter_recipe_ingredient'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='prepare',
            field=models.IntegerField(default=10),
            preserve_default=False,
        ),
    ]
