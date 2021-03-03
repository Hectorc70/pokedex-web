# Generated by Django 3.1.6 on 2021-03-03 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pokemon',
            fields=[
                ('id_poke', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('path_sprite', models.ImageField(upload_to='sprites/')),
            ],
        ),
    ]