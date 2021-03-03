from django.db import models

# Create your models here.


class Pokemon(models.Model):
    id_poke = models.AutoField(auto_created=True,primary_key=True, unique=True)
    name = models.CharField(max_length=100, blank=False)
    path_sprite = models.CharField(max_length=500, blank=False)


