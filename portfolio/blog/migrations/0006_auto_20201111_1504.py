# Generated by Django 3.1.3 on 2020-11-11 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20201111_1423'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=60, unique=True, verbose_name='Title'),
        ),
    ]
