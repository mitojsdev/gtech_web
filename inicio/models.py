from django.db import models

# Create your models here.


class Usuario(models.Model):
    cpf = models.CharField(max_length=11, unique=True)
    senha = models.CharField(max_length=100)

    def __str__(self):
        return self.cpf
    

class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True)    
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=15)
    data_cadastro = models.DateField()

    class Meta:
        db_table = "TB_CLIENTE"  # Faz referência à tabela existente no banco de dados

    def __str__(self):
        return self.nome
