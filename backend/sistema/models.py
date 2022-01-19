from django.db import models

# Create your models here.
class Pessoa(models.Model):
    nome = models.CharField(max_length=30)
    sobrenome = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    senha = models.CharField(max_length=30)

    def getJson(self):
        return {"nome":self.nome,"sobrenome":self.sobrenome,"email":self.email,"senha":self.senha}
