# Generated by Django 4.1 on 2022-09-08 06:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_rename_expense_image_expense_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='expense',
            options={'ordering': ('title', 'price')},
        ),
    ]
