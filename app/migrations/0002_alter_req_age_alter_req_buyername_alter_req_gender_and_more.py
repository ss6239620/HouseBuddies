# Generated by Django 4.1.5 on 2023-04-15 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='req',
            name='age',
            field=models.TextField(default=0),
        ),
        migrations.AlterField(
            model_name='req',
            name='buyername',
            field=models.TextField(default=0),
        ),
        migrations.AlterField(
            model_name='req',
            name='gender',
            field=models.TextField(default=0),
        ),
        migrations.AlterField(
            model_name='req',
            name='ownername',
            field=models.TextField(default=0),
        ),
        migrations.AlterField(
            model_name='req',
            name='qualification',
            field=models.TextField(default=0),
        ),
    ]
