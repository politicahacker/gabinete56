from django.db import models

class StringField(models.TextField):
    def formfield(self, **kwargs):
        kwargs['widget'] = widgets.AdminTextInputWidget
        return super(StringField, self).formfield(**kwargs)

# Create your models here.
class Partido(models.Model):
    nome = StringField()
    sigla =StringField()
    logo = models.ImageField(blank=True, upload_to='partidos')

class Vereador(models.Model):
    nome = StringField()
    partido = models.ForeignKey(Partido)

class Local(models.Model):
    nome = StringField()

class Agenda(models.Model):
    horario_inicio = models.DateTimeField()
    horario_fim = models.DateTimeField()
    descricao = models.TextField()
    local = models.ForeignKey(Local)
    vereador = models.ForeignKey(Vereador)