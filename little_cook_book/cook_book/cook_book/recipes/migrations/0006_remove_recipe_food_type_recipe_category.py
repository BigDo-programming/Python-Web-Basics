# Generated by Django 4.1.2 on 2022-10-13 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0005_recipe_prepare'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='food_type',
        ),
        migrations.AddField(
            model_name='recipe',
            name='category',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8)], default=2),
            preserve_default=False,
        ),
    ]
