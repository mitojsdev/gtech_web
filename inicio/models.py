from django.db import models

# Create your models here.


class Usuario(models.Model):
    cpf = models.CharField(max_length=11, unique=True)
    senha = models.CharField(max_length=100)

    def __str__(self):
        return self.cpf
