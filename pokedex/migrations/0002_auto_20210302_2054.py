# Generated by Django 3.1.6 on 2021-03-03 02:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokedex', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='path_sprite',
            field=models.CharField(max_length=500),
        ),
    ]
