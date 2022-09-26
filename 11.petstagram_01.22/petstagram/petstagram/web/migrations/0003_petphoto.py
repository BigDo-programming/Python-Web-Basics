# Generated by Django 4.1.1 on 2022-09-19 07:08

from django.db import migrations, models
import petstagram.web.models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_alter_pet_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='PetPhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='', validators=[petstagram.web.models.validate_file_max_size_in_mb])),
                ('description', models.TextField(blank=True, null=True)),
                ('publication_date', models.DateTimeField(auto_now_add=True)),
                ('likes', models.IntegerField(default=0)),
                ('tagged_pets', models.ManyToManyField(to='web.pet')),
            ],
        ),
    ]