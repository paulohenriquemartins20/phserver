from django.db import models

# Create your models here.



class Usuarios(models.Model):

    id_usuarios = models.AutoField(primary_key=True)

    nome = models.TextField(max_length=288)

    idade = models.IntegerField()

    cpf = models.IntegerField()

