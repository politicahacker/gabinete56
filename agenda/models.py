from django.db import models
from politicos.models import Partido, Politico, StringField

class Local(models.Model):
    nome = StringField(primary_key=True)

    def __str__(self):
        return self.nome

class Evento(models.Model):
    data = models.DateTimeField()
    descricao = models.TextField(primary_key=True)
    local = models.ForeignKey(Local)
    vereador = models.ForeignKey(Politico)