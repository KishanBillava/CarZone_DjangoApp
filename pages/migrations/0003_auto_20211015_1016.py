# Generated by Django 3.0.7 on 2021-10-15 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_auto_20211014_1840'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='photo',
            field=models.ImageField(upload_to='photos/%Y/%m/%d'),
        ),
    ]