# Generated by Django 4.1 on 2022-09-13 08:37

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newApp', '0002_remove_book_author_book_published_delete_student'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='ratings',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)]),
        ),
    ]
