from django.db import models

# Create your models here.


class Pokemon(models.Model):
    id_poke = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=False)
    path_sprite = models.ImageField(upload_to='sprites/')


